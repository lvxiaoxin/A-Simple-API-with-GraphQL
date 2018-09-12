# -*- coding: utf-8 -*-
"""
@version: 
@time: 2018/9/12
@author: lvxiaoxin
@software: PyCharm
@file: schema
"""

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from databases import db_session
from models import Families as FamiliesModel, Members as MembersModel

__author__ = 'lvxin'


class Families(SQLAlchemyObjectType):
    class Meta:
        model = FamiliesModel
        interface = (relay.Node,)


class FamiliesConnection(SQLAlchemyConnectionField):
    class Meta:
        node = Families


class Members(SQLAlchemyObjectType):
    class Meta:
        model = MembersModel
        interface = (relay.Node,)


class MembersConnection(SQLAlchemyConnectionField):
    class Meta:
        node = Members


class CreateMember(graphene.Mutation):
    class Input:
        name = graphene.String()
        gender = graphene.String()
        families_id = graphene.Int()

    ok = graphene.Boolean()
    member = graphene.Field(Members)

    @classmethod
    def mutate(cls, _, args, context, info):
        member = Members(name=args.get('name'), gender=args.get('gender'), families_id=args.get('families_id'))
        db_session.add(member)
        db_session.commit()
        ok = True
        return CreateMember(member=member, ok=ok)


class CreateFamily(graphene.Mutation):
    class Input:
        name = graphene.String()
        rank = graphene.Int()

    ok = graphene.Boolean()
    family = graphene.Field(Families)

    @classmethod
    def mutate(cls, _, args, context, info):
        family = Families(name=args.get('name'), rank=args.get('rank'))
        db_session.add(family)
        db_session.commit()
        ok = True
        return CreateFamily(family=family, ok=ok)


class MyMutations(graphene.ObjectType):
    create_member = CreateMember.Field()
    create_family = CreateFamily.Field()


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_members = SQLAlchemyConnectionField(MembersConnection)
    all_families = SQLAlchemyConnectionField(FamiliesConnection)


schema = graphene.Schema(query=Query, mutation=MyMutations, types=[Families, Members])

