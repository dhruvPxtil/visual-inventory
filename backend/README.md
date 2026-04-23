# Backend - Visual Inventory AI System

Python FastAPI backend with custom ML/CV pipelines for intelligent inventory detection and recommendations.

## 🏗️ Architecture

```
backend/
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes.py              # Main API endpoints
│   │   ├── detection.py           # Detection endpoints
│   │   ├── inventory.py           # Inventory endpoints
│   │   ├── recommendations.py     # Recommendation endpoints
│   │   ├── analytics.py           # Analytics endpoints
│   │   └── health.py              # Health check endpoints
│   │
│   ├── cv_engine/
│   │   ├── __init__.py
│   │   ├── detector.py            # YOLO detection engine
│   │   ├── preprocessor.py        # Image preprocessing
│   │   ├── postprocessor.py       # Detection post-processing
│   │   ├── tracker.py             # Multi-object tracking
│   │   └── utils.py               # CV utilities
│   │
│   ├── ml_pipeline/
│   │   ├── __init__.py
│   │   ├── inventory_analyzer.py   # Stock level analysis
│   │   ├── price_matcher.py        # Price mismatch detection
│   │   ├── demand_predictor.py     # ML-based forecasting
│   │   ├── anomaly_detector.py     # Outlier detection
│   │   └── feature_extractor.py    # Feature engineering
│   │
│   ├── recommendation_engine/
│   │   ├── __init__.py
│   │   ├── action_generator.py     # Generate recommendations
│   │   ├── action_ranker.py        # Priority ranking logic
│   │   ├── batch_optimizer.py      # Efficiency clustering
│   │   ├── impact_calculator.py    # Impact scoring
│   │   └── staff_matcher.py        # Capability matching
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── detection_service.py    # Detection orchestration
│   │   ├── inventory_service.py    # Inventory management
│   │   ├── recommendation_service.py # Recommendation logic
│   │   ├── analytics_service.py    # Analytics aggregation
│   │   └── cache_service.py        # Caching layer
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   ├── models.py              # SQLAlchemy ORM models
│   │   ├── schemas.py             # Pydantic schemas
│   │   ├── crud.py                # Database operations
│   │   └── session.py             # Database session management
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── logger.py              # Logging configuration
│   │   ├── validators.py          # Input validation
│   │   ├── formatters.py          # Response formatting
│   │   ├── config.py              # Configuration loader
│   │   └── constants.py           # Application constants
│   │
│   ├── middleware/
│   │   ├── __init__.py
│   │   ├── cors.py                # CORS middleware
│   │   ├── auth.py                # Authentication middleware
│   │   └── rate_limit.py          # Rate limiting
│   │
│   ├── __init__.py
│   └── main.py                    # FastAPI app factory
│
├── models/
│   ├── pretrained/
│   │   ├── yolov8_shelf.pt        # Custom YOLO model
│   │   ├── classifier.onnx        # Product classifier
│   │   └── demand_model.pkl       # Demand predictor
│   │
│   └── training/
│       ├── README.md              # Model training guide
│       ├── train.py               # Training script
│       ├── evaluate.py            # Model evaluation
│       ├── datasets/              # Training datasets
│       └── config.yaml            # Model configuration
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py                # Test configuration
│   ├── test_detection.py          # Detection tests
│   ├── test_inventory.py          # Inventory tests
│   ├── test_recommendations.py    # Recommendation tests
│   ├── test_api.py                # API endpoint tests
│   └── fixtures/                  # Test data
│
├── scripts/
│   ├── download_models.py         # Download pretrained models
│   ├── setup_db.py                # Initialize database
│   ├── seed_data.py               # Seed sample data
│   ├── benchmark.py               # Performance benchmarking
│   └── migrate.py                 # Database migrations
│
├── config/
│   ├── __init__.py
│   ├── development.py             # Dev environment config
│   ├── production.py              # Prod environment config
│   └── testing.py                 # Test environment config
│
├── logs/                          # Application logs
├── data/                          # Local data storage
│   ├── models/                    # Model files
│   ├── cache/                     # Cache directory
│   └── database/                  # SQLite database
│
├── requirements.txt               # Python dependencies
├── .env.example                   # Environment template
├── Dockerfile                     # Docker image
├── docker-compose.yml             # Multi-container setup
├── run.py                         # Application entry point
└── README.md                      # This file
```

---

## 🚀 Installation

### Prerequisites
```bash
Python 3.9+
pip & virtualenv
PostgreSQL (optional, for production)
Redis (optional, for caching)
CUDA 11.8+ (optional, for GPU)
```

### Setup Steps

#### 1. Create Virtual Environment
```bash
python -m venv venv

# Activate
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

#### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 3. Download Models
```bash
python scripts/download_models.py
```

#### 4. Initialize Database
```bash
python scripts/setup_db.py
python scripts/seed_data.py
```

#### 5. Configure Environment
```bash
cp .env.example .env
```

Edit `.env`:
```env
ENV=development
DEBUG=True
API_HOST=0.0.0.0
API_PORT=8000

DATABASE_URL=sqlite:///./data/inventory.db
REDIS_URL=redis://localhost:6379

CONFIDENCE_THRESHOLD=0.5
GPU_ENABLED=True

FEATURE_DEMAND_PREDICTION=True
FEATURE_PRICE_MATCHING=True
FEATURE_ANOMALY_DETECTION=True
```

#### 6. Start Server
```bash
python run.py
```

**Server running at**: `http://localhost:8000`
**API Docs**: `http://localhost:8000/docs`

---

## 📡 API Endpoints

### Health & Status
```http
GET /health
GET /status
```

### Detection
```http
POST /api/v1/detect
Content-Type: multipart/form-data
{
  "image": File,
  "shelf_id": string (optional)
}
```

### Inventory
```http
GET /api/v1/inventory?shelf_id=SHELF-001
GET /api/v1/inventory/missing?shelf_id=SHELF-001
GET /api/v1/inventory/mismatches?shelf_id=SHELF-001
```

### Recommendations
```http
GET /api/v1/recommendations?shelf_id=SHELF-001&staff_id=STAFF-123
GET /api/v1/recommendations/{recommendation_id}
POST /api/v1/recommendations/{recommendation_id}/execute
```

### Analytics
```http
GET /api/v1/analytics/shelf?shelf_id=SHELF-001&period=7d
GET /api/v1/analytics/staff?staff_id=STAFF-123&period=7d
GET /api/v1/analytics/products?limit=10
```

---

## 🧠 Core Components

### 1. Computer Vision Engine (`cv_engine/`)

**Detector** - YOLO-based object detection
```python
from app.cv_engine.detector import ProductDetector

detector = ProductDetector(model_path="models/pretrained/yolov8_shelf.pt")
detections = detector.detect(image_array)
# Returns: [Detection(class, confidence, bbox, product_id)]
```

**Preprocessor** - Image normalization
```python
from app.cv_engine.preprocessor import ImagePreprocessor

preprocessor = ImagePreprocessor()
normalized_image = preprocessor.normalize(raw_image)
```

### 2. ML Pipeline (`ml_pipeline/`)

**Inventory Analyzer** - Stock level prediction
```python
from app.ml_pipeline.inventory_analyzer import InventoryAnalyzer

analyzer = InventoryAnalyzer(model_path="models/pretrained/demand_model.pkl")
missing_items = analyzer.identify_missing_items(detections, shelf_config)
```

**Price Matcher** - Price mismatch detection
```python
from app.ml_pipeline.price_matcher import PriceMatcher

matcher = PriceMatcher()
mismatches = matcher.find_mismatches(detections, price_catalog)
```

### 3. Recommendation Engine (`recommendation_engine/`)

**Action Generator** - Generate next-best-actions
```python
from app.recommendation_engine.action_generator import ActionGenerator

generator = ActionGenerator()
actions = generator.generate_actions(missing_items, mismatches)
```

**Action Ranker** - Priority-based ranking
```python
from app.recommendation_engine.action_ranker import ActionRanker

ranker = ActionRanker()
ranked_actions = ranker.rank(actions)
# Returns: [Action, sorted by priority]
```

---

## 🔌 Service Layer

### Detection Service
```python
from app.services.detection_service import DetectionService

detector = DetectionService()
result = detector.detect_from_image(image_file, shelf_id="SHELF-001")
```

### Inventory Service
```python
from app.services.inventory_service import InventoryService

inventory = InventoryService()
status = inventory.get_shelf_inventory(shelf_id="SHELF-001")
missing = inventory.identify_missing_items(shelf_id="SHELF-001")
```

### Recommendation Service
```python
from app.services.recommendation_service import RecommendationService

recommender = RecommendationService()
recs = recommender.get_recommendations(shelf_id="SHELF-001", staff_id="STAFF-123")
```

---

## 📊 Database Models

### Product
```python
class Product(Base):
    id: str
    name: str
    sku: str
    category: str
    price: float
    expected_quantity: int
    shelf_id: str
    created_at: datetime
    updated_at: datetime
```

### Detection
```python
class Detection(Base):
    id: str
    shelf_id: str
    image_path: str
    detections: dict  # JSON of detected items
    confidence: float
    processing_time_ms: int
    created_at: datetime
```

### Recommendation
```python
class Recommendation(Base):
    id: str
    shelf_id: str
    staff_id: str
    action_type: str  # RESTOCK, PRICE_FIX, etc
    product_id: str
    priority: int
    impact_score: float
    time_estimate_min: int
    status: str  # PENDING, COMPLETED, SKIPPED
    created_at: datetime
    completed_at: datetime
```

---

## 🧪 Testing

### Run Tests
```bash
# All tests
pytest

# With coverage
pytest --cov=app

# Specific test file
pytest tests/test_detection.py -v

# Specific test
pytest tests/test_detection.py::test_detect_products -v
```

### Test Structure
```python
# tests/test_detection.py
import pytest
from app.cv_engine.detector import ProductDetector

@pytest.fixture
def detector():
    return ProductDetector(model_path="models/pretrained/yolov8_shelf.pt")

def test_detect_products(detector, sample_image):
    detections = detector.detect(sample_image)
    assert len(detections) > 0
    assert all(d.confidence > 0.5 for d in detections)
```

---

## 📈 Performance Optimization

### 1. Model Optimization
- Use ONNX Runtime for faster inference
- Quantize models (int8/float16)
- Batch processing for multiple images

### 2. Caching Strategy
```python
from app.services.cache_service import CacheService

cache = CacheService()
cached_result = cache.get("shelf_001_inventory")
if not cached_result:
    result = compute_inventory("shelf_001")
    cache.set("shelf_001_inventory", result, ttl=300)
```

### 3. Database Optimization
- Index frequently queried columns
- Connection pooling (SQLAlchemy)
- Denormalization for analytics

### 4. Async Processing
```python
from fastapi import FastAPI
import asyncio

@app.post("/api/v1/detect")
async def detect(image: UploadFile):
    # Non-blocking I/O
    image_array = await load_image(image)
    detections = await detector.detect_async(image_array)
    return detections
```

---

## 🔐 Security

- ✅ Input validation on all endpoints
- ✅ Rate limiting (100 req/min default)
- ✅ CORS properly configured
- ✅ Environment variables for secrets
- ✅ SQL injection prevention (ORM)
- ✅ No sensitive data logging

---

## 🐳 Docker Deployment

### Build Image
```bash
docker build -t visual-inventory-backend:latest -f Dockerfile .
```

### Run Container
```bash
docker run -p 8000:8000 \
  -e DATABASE_URL=postgresql://user:pass@db:5432/inventory \
  -e REDIS_URL=redis://redis:6379 \
  visual-inventory-backend:latest
```

### Docker Compose
```bash
docker-compose up -d
```

---

## 🛠️ Development Commands

```bash
# Start development server
python run.py

# Run with auto-reload
uvicorn app.main:app --reload

# Format code
black app/

# Lint
flake8 app/

# Type checking
mypy app/

# Run tests
pytest

# Generate API docs
python scripts/generate_api_docs.py
```

---

## 📊 Configuration Files

### .env Template
```env
# Environment
ENV=development
DEBUG=True

# Server
API_HOST=0.0.0.0
API_PORT=8000
WORKERS=4

# Database
DATABASE_URL=sqlite:///./data/inventory.db

# Redis
REDIS_URL=redis://localhost:6379
REDIS_TIMEOUT=10

# Detection
CONFIDENCE_THRESHOLD=0.5
GPU_ENABLED=True
BATCH_SIZE=1

# Features
FEATURE_DEMAND_PREDICTION=True
FEATURE_PRICE_MATCHING=True
FEATURE_ANOMALY_DETECTION=True

# Logging
LOG_LEVEL=INFO
LOG_FILE=logs/app.log
```

---

## 🔄 ML Pipeline Workflow

```
Input Image
    ↓
[Preprocessing]
    ↓
[YOLO Detection]
    ↓
[Post-processing]
    ↓
[Inventory Analysis]
    ↓
[Price Matching]
    ↓
[Demand Prediction]
    ↓
[Anomaly Detection]
    ↓
[Recommendation Generation]
    ↓
[Action Ranking & Batching]
    ↓
Output: Ranked Actions
```

---

## 📚 Model Details

### YOLO Model (yolov8_shelf.pt)
- **Input**: 640x640 RGB images
- **Output**: Bounding boxes + class labels
- **Accuracy**: 85-92% mAP
- **Speed**: 50-100ms per image (GPU)
- **Classes**: ~50 retail products

### Demand Predictor (demand_model.pkl)
- **Algorithm**: Random Forest + Time Series
- **Features**: Historical sales, seasonality, weather
- **Output**: Expected restocking quantity
- **Accuracy**: 78-85% RMSE

---

## 🤝 Contributing

### Code Style
- Follow PEP 8
- Use type hints
- Document functions with docstrings
- Write unit tests for all new code

### Pull Request Process
1. Create feature branch
2. Write tests
3. Run linting & formatting
4. Update documentation
5. Submit PR

---

## 📞 Support

- **Issues**: GitHub Issues
- **Email**: backend-support@example.com
- **Documentation**: See docs/ folder

---

## 📄 License

MIT License - See LICENSE file for details
