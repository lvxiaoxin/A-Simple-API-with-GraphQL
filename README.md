# A-Simple-API-with-GraphQL
A simple API with GraphQL

Based on **Flask**, **Graphene(1.4)**, and **SQLAlchemy**

## Introduction

This project is a simple demo for using graphene, which is a server side 
implementation of GraphQL, to build a server supporting GraphQL query and other operations.

The project generates a SQLite database, with 2 tables, including `families` and `members`.

The background is based on **The Game of Throne**.

## Usage

To run the project, just clone the project and run:

> python server

then you can go to *http://127.0.0.1:5000/graphql* to have a try.

## Play with Example

> Get all members

```json
    {
      allMembers {
        edges {
          node {
            name
            gender
            families {
              name
              rank
              house
            }
          }
        }
      }
    }
``` 

> Create a Family

```json
    mutation {
      createFamily(name: "Stark", rank: "1", house: "Winterfell") {
        family {
          name
          rank
          house
        }
        ok
      }
    }

```

> Find a Specific Member

```json
    {
      findMember(name: "Arya Stark") {
        name
        families {
          name
        }
      }
    }

```
