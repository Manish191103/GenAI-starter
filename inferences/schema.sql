-- Database schema for inferences

-- Create inferences table
CREATE TABLE IF NOT EXISTS inferences (
    id SERIAL PRIMARY KEY,
    model_name VARCHAR(255) NOT NULL,
    prompt TEXT NOT NULL,
    response TEXT NOT NULL,
    tokens_used INTEGER,
    latency_ms INTEGER,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    metadata JSONB
);

-- Create index on model_name for faster querying
CREATE INDEX IF NOT EXISTS idx_inferences_model_name ON inferences(model_name);

-- Create index on created_at for time-based queries
CREATE INDEX IF NOT EXISTS idx_inferences_created_at ON inferences(created_at);

COMMENT ON TABLE inferences IS 'Stores AI model inference results and metadata'; 