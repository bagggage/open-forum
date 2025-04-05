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
    throw error;
  }
};

export const registerUser = (email, password, name) =>
  handleRequest(() =>
    apiClient.post('/v1/auth/register', {
      email,
      password,
      is_active: true,
      is_superuser: false,
      is_verified: false,
      name,
    })
  );

export const loginUser = (email, password) =>
  handleRequest(() =>
    apiClient.post(
      '/v1/auth/jwt/login',
      new URLSearchParams({
        username: email,
        password,
        grant_type: 'password',
        scope: '',
        client_id: 'string',
        client_secret: 'string',
      }).toString(),
      {
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      }
    )
  );

export const logoutUser = () =>
  handleRequest(() => apiClient.post('/v1/auth/jwt/logout'));