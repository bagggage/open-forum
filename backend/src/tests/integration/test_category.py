import pytest

class TestCategory:
    category_id = None

    @pytest.mark.order(2)
    @pytest.mark.asyncio
    async def test_get_categories(self, async_client):
        response = await async_client.get("/v1/categories/")

        assert response.status_code == 200
        assert isinstance(response.json(), list)

    @pytest.mark.order(1)
    @pytest.mark.asyncio
    async def test_create_category(self, async_client):
        category_data = {"name": "test_category"}

        response = await async_client.post(
            "/v1/categories/",
            json=category_data
        )

        assert response.status_code == 200
        created_category = response.json()
        TestCategory.category_id = created_category["id"]

    @pytest.mark.order(9)
    @pytest.mark.asyncio
    async def test_get_category(self, async_client):
        assert TestCategory.category_id is not None

        response = await async_client.get(f"/v1/categories/{TestCategory.category_id}")

        assert response.status_code == 200

    @pytest.mark.order(13)
    @pytest.mark.asyncio
    async def test_delete_category(self, async_client):
        assert TestCategory.category_id is not None

        response = await async_client.delete(f"/v1/categories/{TestCategory.category_id}")

        assert response.status_code == 200
