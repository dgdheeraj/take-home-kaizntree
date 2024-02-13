## Testing

Added unit tests for models and views with a 85% coverage
```
coverage run --source main ./manage.py test
coverage report -m
```
<img width="713" alt="coverage_report" src="https://github.com/dgdheeraj/take-home-kaizntree/assets/45272841/ed24739c-0da4-4882-9ebb-40f84554ed67">



## API Documentation

Used Django Session Authentication to authenticate all endpoints
In case of a csrf error while hitting an endpoint, please pass the csrf token from the cookie as a seperate `X-CSRFToken` header (Cookie will be visible in the header directly if postman is being used to test)

### Authentication APIs

#### Register User
- **URL**: `/api/v1/register/`
- **Method**: `POST`
- **Description**: Registers a new user with the provided username and password.
- **Request Body**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Response**:
  - `200 OK`: User successfully registered.
  - `400 Bad Request`: If username or password is missing or username is already taken.

#### Login
- **URL**: `/api/v1/login/`
- **Method**: `POST`
- **Description**: Logs in a user with the provided username and password.
- **Request Body**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Response**:
  - `200 OK`: User successfully logged in.
  - `400 Bad Request`: If username or password is missing or credentials are invalid.

#### Logout
- **URL**: `/api/v1/logout/`
- **Method**: `GET`
- **Description**: Logs out the currently logged-in user.
- **Response**:
  - `200 OK`: User successfully logged out.

#### Check Session
- **URL**: `/api/v1/session/`
- **Method**: `GET`
- **Description**: Checks if the user is authenticated through session.
- **Response**:
  - `200 OK`: If the user is authenticated.
  - `401 Unauthorized`: If the user is not authenticated.

#### Who Am I
- **URL**: `/api/v1/whoami/`
- **Method**: `GET`
- **Description**: Retrieves the username of the currently logged-in user.
- **Response**:
  - `200 OK`: Returns the username of the logged-in user.
  - `401 Unauthorized`: If the user is not authenticated.

### APIs for Tags, Category, Inventory

#### Tags
- **URL**: `/api/v1/tag`
- **Method**: `GET`, `POST`
- **Description**:
  - `GET`: Retrieves all tags.
  - `POST`: Creates a new tag.
- **Request Body** (for `POST`):
  ```json
  {
    "name": "string"
  }
  ```
- **Response**:
  - `200 OK`: Returns tag data for `GET`, or confirms tag creation for `POST`.
  - `400 Bad Request`: If there's an error creating a tag.

#### Category
- **URL**: `/api/v1/category`
- **Method**: `GET`, `POST`
- **Description**:
  - `GET`: Retrieves all categories.
  - `POST`: Creates a new category.
- **Request Body** (for `POST`):
  ```json
  {
    "name": "string"
  }
  ```
- **Response**:
  - `200 OK`: Returns category data for `GET`, or confirms category creation for `POST`.
  - `400 Bad Request`: If there's an error creating a category.

#### Inventory
- **URL**: `/api/v1/inventory`
- **Method**: `GET`, `POST`
- **Description**:
  - `GET`: Retrieves all inventory items with optional filtering.
  - `POST`: Creates a new inventory item.
- **Query Parameters** (for `GET`):
  - `sku`: Filter by SKU.
  - `name`: Filter by name.
  - `category`: Filter by category name.
  - `tag`: Filter by tag name.
  - `sort_by`: Sort by a field.
  - `order`: Sort order (`asc` or `desc`).
  - `stock_status`: Filter by stock status.
- **Request Body** (for `POST`):
  ```json
  {
    "SKU":"Entry 1",
    "name":"Etsy Bundle Pack 2",
    "tags":["etsy"],
    "category":"Bundles",
    "author": "abc",
    "in_stock": 0,
    "available_stock": 0
  }
  ```
- **Response**:
  - `200 OK`: Returns inventory data for `GET`, or confirms inventory creation for `POST`.
  - `400 Bad Request`: If there's an error creating an inventory item.
