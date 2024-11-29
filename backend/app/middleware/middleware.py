# app/middleware.py
from starlette.middleware.base import BaseHTTPMiddleware

class ContentSecurityPolicyMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, policy: str = "default-src 'self';"):
        super().__init__(app)
        self.policy = policy  # Asegúrate de guardar el parámetro policy

    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers['Content-Security-Policy'] = self.policy  # Establecer el header
        return response
