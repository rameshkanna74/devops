# Stage 1: Build dependencies
FROM python:3.12-slim AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN python -m venv /opt/venv
# Enable venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.12-slim

WORKDIR /app

# Install runtime dependencies (e.g., libpq for psycopg2 if used)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

# Copy virtual env from builder
COPY --from=builder /opt/venv /opt/venv
# Enable venv
ENV PATH="/opt/venv/bin:$PATH"

# Create a non-root user and group
RUN addgroup --system appgroup && adduser --system --group appuser

# Copy application code
COPY . .

# Change ownership to non-root user
RUN chown -R appuser:appgroup /app

# Switch to non-root user
USER appuser

EXPOSE 8000

# Run using the uvicorn from venv
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]