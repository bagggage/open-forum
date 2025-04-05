import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000',
  withCredentials: true,
});

const handleRequest = async (request) => {
  try {
    const response = await request();
    return response.data;
  } catch (error) {
    console.error('API Error:', error);
    if (error.response) {
      console.error('Response Data:', error.response.data);
      console.error('Status Code:', error.response.status);
    } else if (error.request) {
      console.error('No response received:', error.request);
    } else {
      console.error('Error Message:', error.message);
    }
    throw error;
  }
};

export const fetchCategories = () =>
  handleRequest(() => apiClient.get('/v1/categories'));

export const fetchQuestions = (skip = 0, limit = 10) =>
  handleRequest(() => apiClient.get('/v1/questions/', { params: { skip, limit } }));

export const fetchQuestionsByCategory = (categoryName, skip = 0, limit = 10) =>
  handleRequest(() => apiClient.get('/v1/questions/by-category/', { params: { category: categoryName, skip, limit } }));