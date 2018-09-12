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
        interfaces = (relay.Node,)


class FamiliesConnections(relay.Connection):
    class Meta:
        node = Families


class Members(SQLAlchemyObjectType):
    class Meta:
        model = MembersModel
        interfaces = (relay.Node,)


class MembersConnections(relay.Connection):
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
        member = MembersModel(name=args.get('name'), gender=args.get('gender'), families_id=args.get('families_id'))
        db_session.add(member)
        db_session.commit()
        ok = True
        return CreateMember(member=member, ok=ok)


class CreateFamily(graphene.Mutation):
    class Input:
        name = graphene.String()
        rank = graphene.Int()
        house = graphene.String()

    ok = graphene.Boolean()
    family = graphene.Field(Families)

    @classmethod
    def mutate(cls, _, args, context, info):
        family = FamiliesModel(name=args.get('name'), rank=args.get('rank'), house=args.get('house'))
        db_session.add(family)
        db_session.commit()
        ok = True
        return CreateFamily(family=family, ok=ok)


class MyMutations(graphene.ObjectType):
    create_member = CreateMember.Field()
    create_family = CreateFamily.Field()


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    members = SQLAlchemyConnectionField(Members)
    families = SQLAlchemyConnectionField(Families)
    all_members = SQLAlchemyConnectionField(MembersConnections)
    all_families = SQLAlchemyConnectionField(FamiliesConnections)
    find_member = graphene.Field(lambda: Members, name=graphene.String())
    find_family = graphene.Field(lambda: Families, name=graphene.String())

    def resolve_find_member(self, args, context, info):
        query = Members.get_query(context)
        name = args.get('name')
        return query.filter(MembersModel.name == name).first()

    def resolve_find_family(self, args, context, info):
        query = Families.get_query(context)
        name = args.get('name')
        return query.filter(FamiliesModel.name == name).first()


schema = graphene.Schema(query=Query, mutation=MyMutations,
                         types=[Families, Members, FamiliesConnections, MembersConnections])
