import pytest

class TestQuestion:
    question_id = None

    @pytest.mark.order(7)
    @pytest.mark.asyncio
    async def test_get_questions(self, async_client):
        response = await async_client.get("/v1/questions/")
    
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    @pytest.mark.order(6)
    @pytest.mark.asyncio
    async def test_get_questions_by_category_name(self, async_client):
        CATEGORY_NAME = "test_category"
    
        response = await async_client.get(f"/v1/questions/by-category/?category={CATEGORY_NAME}")
    
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        
    @pytest.mark.order(5)
    @pytest.mark.asyncio
    async def test_create_question(self, async_client, auth_cookie):
        test_question_data = {
            "title": "Test Question",
            "text": "This is a test question.",
            "category_name": "test_category",
            "tag_names": ["test_tag"]
        }

        response = await async_client.post(
            "/v1/questions/",
            json=test_question_data,
            cookies=auth_cookie
        )

        assert response.status_code == 200

        TestQuestion.question_id = response.json()["id"]
        pytest.question_id = TestQuestion.question_id

    @pytest.mark.order(10)
    @pytest.mark.asyncio
    async def test_get_question(self, async_client):
        assert TestQuestion.question_id is not None

        response = await async_client.get(f"/v1/questions/{TestQuestion.question_id}")

        assert response.status_code == 200

    @pytest.mark.order(15)
    @pytest.mark.asyncio
    async def test_update_question(self, async_client, auth_cookie):
        assert TestQuestion.question_id is not None

        updated_data = {
            "title": "Updated Title",
            "text": "Updated text for the question"
        }

        response = await async_client.put(
            f"/v1/questions/{TestQuestion.question_id}",
            json=updated_data,
            cookies=auth_cookie
        )

        assert response.status_code == 200

    @pytest.mark.order(17)
    @pytest.mark.asyncio
    async def test_delete_question(self, async_client, auth_cookie):
        assert TestQuestion.question_id is not None

        response = await async_client.delete(
            f"/v1/questions/{TestQuestion.question_id}",
            cookies=auth_cookie
        )
        
        assert response.status_code == 200
