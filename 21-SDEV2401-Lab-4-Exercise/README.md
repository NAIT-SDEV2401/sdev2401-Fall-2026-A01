# SDEV 2401 - Lab 4 Exercise: REST APIs with Django

In this exercise, you will create a simple REST API using Django and the Django REST Framework. This time you'll use the `FoundItem` model to keep track of items turned in at the campus lost and found.

## Instructions

### Part 1: Create the serializer, endpoints, and URLs for the FoundItem model.

#### 0. Get your project ready, and load the data.

- Install the requirements in a virtual environment named `venv`.
- From the directory containing `manage.py`, make and apply migrations.
- Run the development server.

#### 1. Run the management command to load the initial data.

- Look at the `load_found_items` management command in `app_found_items/management/commands/load_found_items.py`.
    - This creates three found items in the database for you to work with.
- Run `python manage.py load_found_items`.
- Create a superuser account with `python manage.py createsuperuser`.
    - Verify that the data has been loaded by logging in at <http://localhost:8000/admin/> and opening **Found items**.

#### 2. Create a serializer for the FoundItem model.

- In `app_found_items/serializers.py`, create a `ModelSerializer` named `FoundItemSerializer`.
- Include all fields from the `FoundItem` model.
- Add a `validate_item_name` method to check that the item name is not empty or just spaces.
    - Raise `serializers.ValidationError` if the name is invalid. Otherwise, return the value as is.
    - The model allows a blank name. Set up the serializer so that a name is required when creating an item, but a blank string still gets passed to your validation method. In a serializer, `required` checks whether the field was sent and `allow_blank` checks whether it can contain an empty string.

#### 3. Create the API view for the FoundItem model using APIView.

- In `app_found_items/views.py`, create a view named `FoundItemListAPIView` that inherits from `APIView`.
- On the `FoundItemListAPIView`, implement the `get` method with the parameters `self`, `request`, and `pk=None`.
    - If a `pk` is provided, return the found item with that primary key. If it doesn't exist, return a 404 response.
    - If no `pk` is provided, return a list of all found items.
    - Use `FoundItemSerializer` to serialize the data. Use `many=True` when serializing the list.
- Implement `post` for the list endpoint.
    - Use `FoundItemSerializer` to deserialize the data from the request.
    - If the data is valid, save the new found item and return it with a 201 status code.
    - If the data is not valid, return the errors with a 400 status code.
- Implement `patch` for the detail endpoint.
    - Retrieve the found item with the provided primary key. If it doesn't exist, return a 404 response.
    - Pass the existing item and the request data to `FoundItemSerializer`. Set `partial=True` so you can update just one field.
    - If the data is valid, save the changes and return the updated item with a 200 status code.
    - If the data is not valid, return the errors with a 400 status code.

#### 4. Create the URL patterns for the FoundItem API view.

- In `app_found_items/urls.py`, create a URL pattern at `found-items/` for the list and another at `found-items/<int:pk>/` for the detail view. Both patterns use `FoundItemListAPIView.as_view()`.
- In the main project's `lost_and_found_project/urls.py` file, include the `app_found_items` URLs under `v1/api/`.

#### 5. Test the FoundItem API endpoints using curl or Postman.

Use `http://localhost:8000` and send `Content-Type: application/json` with requests that have a JSON body.

1. Send a GET request to `/v1/api/found-items/` and verify that it returns all found items.
2. Send a GET request to `/v1/api/found-items/<pk>/`, replacing `<pk>` with an ID from the list. Try it again with an ID that doesn't exist.
3. Send a POST request to `/v1/api/found-items/` with the JSON below. Try it again with an empty name.
4. Use the ID from your successful POST to send a PATCH request to `/v1/api/found-items/<pk>/`. Set `claimed` to `true`.

## Expected output

### Part 1: get all found items

Expect `200 OK` and a JSON array. If you've just loaded the sample data, there should be three items.

### Part 1: get a single found item

Expect `200 OK` and a single item for an ID that exists. For example, the water bottle might look like this.

```json
{
    "id": 1,
    "item_name": "Blue water bottle",
    "found_at": "Library study area",
    "claimed": false
}
```

Expect `404 Not Found` for an ID that doesn't exist.

### Part 1: create a new found item

Send the following data.

```json
{
    "item_name": "Set of keys",
    "found_at": "Gym reception",
    "claimed": false
}
```

Expect `201 Created` and the new item, including its ID. Send the same data with `"item_name": ""` and expect `400 Bad Request` with an error for `item_name`.

### Part 1: update a found item

Send the following data to mark the item as claimed.

```json
{
    "claimed": true
}
```

Expect `200 OK` with the updated item. The ID, name, and location should stay the same. Send a GET request for that item to check that the change was saved.

## Challenge (optional)

- Create a frontend that lists found items, adds new items, and marks items as claimed.
- Add query parameters to filter by whether an item has been claimed and to search by item name or location.
