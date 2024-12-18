# Test Server API

API Documentation

# Base URL


| URL | Description |
|-----|-------------|
| http://localhost:8080 | Generated server url |


# Authentication



## Security Schemes

| Name              | Type              | Description              | Scheme              | Bearer Format             |
|-------------------|-------------------|--------------------------|---------------------|---------------------------|
| jwt | http |  | bearer | JWT |

# APIs

## PUT /example/example-users/{id}

예제사용자를 업데이트한다.



### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | integer | True | 예제사용자의 아이디 |


### Request Body

[ExampleUserUpdateModel](#exampleuserupdatemodel)





### Responses

#### 200


OK


[ExampleUserResponseModel](#exampleuserresponsemodel)





## DELETE /example/example-users/{id}

예제사용자를 삭제한다.



### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | integer | True | 예제사용자의 아이디 |


### Responses

#### 200


OK




## GET /example/example-users/

List



### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| page | integer |  | Zero-based page index (0..N) |
| size | integer |  | The size of the page to be returned |
| sort | array |  | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. |


### Responses

#### 200


OK


[PageExampleUserResponseModel](#pageexampleuserresponsemodel)





## POST /example/example-users/

Create new User





### Request Body

[ExampleUserCreateModel](#exampleusercreatemodel)





### Responses

#### 200


OK


[ExampleUserResponseModel](#exampleuserresponsemodel)





## GET /example/example-users/test/hello

사용자 이름을 받아 사용자에 대한 인사말을 리턴한다.



### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| name | string | True | 사용자 이름 |


### Responses

#### 200


사용자에 대한 인사말


string





## GET /example/example-users/test/hello2

사용자 이름을 받아 사용자에 대한 인사말을 리턴한다.



### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| userName | object | True | 사용자 인사말과 사용자명 |


### Request Body

[UserName](#username)




Examples




soonoh


```json
{
  "greeting": "Hello",
  "name": "Soonoh"
}
```



### Responses

#### default


사용자명과 인사말


[UserName](#username)




Examples




soonoh


```json
{
  "greeting": "Hello",
  "name": "Soonoh"
}
```



# Components



## ExampleUserUpdateModel


예제사용자 업데이트 요청


| Field | Type | Description |
|-------|------|-------------|
| name | string | 업데이트할 사용자 이름 |


## ExampleUserContactModel



| Field | Type | Description |
|-------|------|-------------|
| name | string |  |
| contactType | string |  |
| value | string |  |


## ExampleUserResponseModel


예제사용자 응답 모델


| Field | Type | Description |
|-------|------|-------------|
| id | integer |  |
| name | string |  |
| contacts | array |  |


## ExampleUserCreateModel


예제사용자 생성 요청


| Field | Type | Description |
|-------|------|-------------|
| name | string |  |
| contacts | array |  |


## UserName


사용자 이름과 인사말


| Field | Type | Description |
|-------|------|-------------|
| greeting | string | 인사말 |
| name | string | 이름 |


## PageExampleUserResponseModel



| Field | Type | Description |
|-------|------|-------------|
| totalPages | integer |  |
| totalElements | integer |  |
| first | boolean |  |
| last | boolean |  |
| size | integer |  |
| content | array |  |
| number | integer |  |
| sort |  |  |
| numberOfElements | integer |  |
| pageable |  |  |
| empty | boolean |  |


## PageableObject



| Field | Type | Description |
|-------|------|-------------|
| offset | integer |  |
| sort |  |  |
| paged | boolean |  |
| unpaged | boolean |  |
| pageNumber | integer |  |
| pageSize | integer |  |


## SortObject



| Field | Type | Description |
|-------|------|-------------|
| empty | boolean |  |
| sorted | boolean |  |
| unsorted | boolean |  |
