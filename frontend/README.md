# Visual Inventory Frontend

React-based real-time camera interface for inventory detection and next-best-action recommendations.

## 📁 Structure

```
frontend/
├── src/
│   ├── components/
│   │   ├── Camera/
│   │   │   ├── CameraFeed.tsx        # Live camera component
│   │   │   ├── DetectionCanvas.tsx   # Overlay detection visualization
│   │   │   └── CameraControls.tsx    # Camera settings
│   │   ├── Detection/
│   │   │   ├── DetectionDisplay.tsx  # Bounding box renderer
│   │   │   ├── ConfidenceIndicator.tsx # Detection confidence UI
│   │   │   └── ClassLabel.tsx        # Product name labels
│   │   ├── Inventory/
│   │   │   ├── InventoryStatus.tsx   # Stock level display
│   │   │   ├── MismatchAlert.tsx     # Price/quantity alerts
│   │   │   └── ShelfSummary.tsx      # Shelf overview
│   │   ├── Recommendations/
│   │   │   ├── ActionCard.tsx        # Single recommendation card
│   │   │   ├── ActionList.tsx        # Ranked action list
│   │   │   ├── PriorityBadge.tsx     # Priority indicator
│   │   │   └── ActionDetails.tsx     # Detailed action info
│   │   ├── Dashboard/
│   │   │   ├── MainDashboard.tsx     # Primary interface
│   │   │   ├── Tabs.tsx              # Tab navigation
│   │   │   ├── SidePanel.tsx         # Info panel
│   │   │   └── TopBar.tsx            # Header/navigation
│   │   ├── Settings/
│   │   │   ├── SettingsPanel.tsx     # Configuration UI
│   │   │   ├── ModelConfig.tsx       # Detection settings
│   │   │   └── CameraCalibration.tsx # Camera calibration
│   │   ├── Common/
│   │   │   ├── Button.tsx            # Button component
│   │   │   ├── Modal.tsx             # Modal dialog
│   │   │   ├── Spinner.tsx           # Loading indicator
│   │   │   └── Toast.tsx             # Notifications
│   │   └── Layout/
│   │       ├── Header.tsx            # App header
│   │       ├── Sidebar.tsx           # Navigation sidebar
│   │       └── Footer.tsx            # Footer
│   ├── hooks/
│   │   ├── useCamera.ts              # Camera access hook
│   │   ├── useDetection.ts           # Detection API hook
│   │   ├── useRecommendations.ts     # Recommendations hook
│   │   ├── useLocalStorage.ts        # Persistent state
│   │   └── useOfflineCache.ts        # Offline caching
│   ├── services/
│   │   ├── api.ts                    # API client
│   │   ├── detection.ts              # Detection service
│   │   ├── inventory.ts              # Inventory service
│   │   ├── recommendations.ts        # Recommendations service
│   │   └── camera.ts                 # Camera utilities
│   ├── utils/
│   │   ├── canvas.ts                 # Canvas drawing utilities
│   │   ├── image.ts                  # Image processing
│   │   ├── validators.ts             # Input validation
│   │   ├── formatters.ts             # Data formatting
│   │   └── constants.ts              # App constants
│   ├── types/
│   │   ├── detection.ts              # Detection types
│   │   ├── inventory.ts              # Inventory types
│   │   ├── recommendation.ts         # Recommendation types
│   │   └── api.ts                    # API types
│   ├── context/
│   │   ├── AppContext.tsx            # Global app state
│   │   ├── DetectionContext.tsx      # Detection state
│   │   └── SettingsContext.tsx       # Settings state
│   ├── styles/
│   │   ├── globals.css               # Global styles
│   │   ├── variables.css             # CSS variables
│   │   └── animations.css            # Animation keyframes
│   ├── App.tsx                       # Main app component
│   ├── main.tsx                      # React entry point
│   └── index.css                     # Root styles
├── public/
│   ├── index.html                    # HTML entry point
│   ├── favicon.ico
│   └── manifest.json                 # PWA manifest
├── package.json
├── tsconfig.json
├── vite.config.ts
├── tailwind.config.js
├── .env.example
└── README.md

```

## 🎯 Core Features

### Real-Time Camera Interface
- WebRTC-based live camera feed
- 30+ FPS performance
- Dual-camera support (front/back on mobile)
- Automatic permission handling

### Live Detection Visualization
- Real-time bounding box overlay
- Confidence score display
- Color-coded detection classes
- Smooth animation rendering

### Inventory Alerts
- Price mismatch notifications
- Stock level warnings
- Missing product alerts
- Toast-based notifications

### Next-Best-Action Dashboard
- Priority-ranked actions
- Estimated completion time
- Batch action grouping
- One-tap action execution

### Settings & Calibration
- Model confidence threshold adjustment
- Camera resolution settings
- Perspective correction
- Offline mode toggle

## 🚀 Quick Start

### Prerequisites
```bash
Node.js >= 16
npm or yarn
```

### Installation

1. **Install dependencies**
```bash
cd frontend
npm install
```

2. **Configure environment**
```bash
cp .env.example .env.local
```

Edit `.env.local`:
```
VITE_API_BASE_URL=http://localhost:8000
VITE_API_TIMEOUT=30000
VITE_ENABLE_OFFLINE=true
VITE_LOG_LEVEL=info
```

3. **Start development server**
```bash
npm run dev
```

Open `http://localhost:5173` in your browser.

4. **Build for production**
```bash
npm run build
npm run preview
```

## 📱 Component Hierarchy

```
App
├── Header
├── MainDashboard
│   ├── Camera Section
│   │   ├── CameraFeed
│   │   ├── DetectionCanvas
│   │   └── CameraControls
│   ├── Detection Results (Tabs)
│   │   ├── InventoryStatus
│   │   │   ├── InventoryStatus
│   │   │   └── MismatchAlert
│   │   ├── Recommendations
│   │   │   ├── ActionCard
│   │   │   └── ActionCard
│   │   └── History
│   ├── SidePanel
│   │   ├── SettingsPanel
│   │   └── CameraCalibration
│   └── BottomNotifications
│       └── Toast
└── Footer
```

## 🎨 UI/UX Design

### Color Scheme
- **Primary**: #2563eb (Blue)
- **Success**: #10b981 (Green)
- **Warning**: #f59e0b (Amber)
- **Danger**: #ef4444 (Red)
- **Background**: #f9fafb (Light Gray)

### Typography
- **Font**: Inter, system fonts
- **Heading**: Bold, 24-32px
- **Body**: Regular, 14-16px
- **Caption**: 12px, gray

### Responsive Design
- Mobile-first approach
- Tablet optimization
- Desktop layout
- Touch-friendly controls

## 🔌 API Integration

### Detection Endpoint
```typescript
POST /api/detect
FormData: { image: File }

Response: {
  detections: Detection[]
  processing_time_ms: number
}
```

### Inventory Endpoint
```typescript
GET /api/inventory?shelf_id=string

Response: {
  shelf_id: string
  total_products: number
  missing_items: MissingItem[]
  price_mismatches: number
}
```

### Recommendations Endpoint
```typescript
GET /api/recommendations?shelf_id=string&staff_id=string

Response: {
  recommendations: Recommendation[]
  batch_efficiency: number
}
```

## 📲 Offline Functionality

- Cache detection results locally
- Store recommendations in IndexedDB
- Sync when connection restored
- PWA-ready with service worker

## 🎥 Camera Handling

```typescript
// Request camera permission
const stream = await navigator.mediaDevices.getUserMedia({
  video: {
    width: { ideal: 1280 },
    height: { ideal: 720 },
    facingMode: 'environment'
  },
  audio: false
});

// Capture frame for detection
const canvas = document.createElement('canvas');
const ctx = canvas.getContext('2d');
ctx.drawImage(videoElement, 0, 0);
const imageData = canvas.toDataURL('image/jpeg');
```

## 🧪 Testing

```bash
# Run tests
npm run test

# Test coverage
npm run test:coverage

# E2E tests
npm run test:e2e
```

## 📦 Dependencies

See `package.json` for complete list. Key packages:
- **react** (UI framework)
- **typescript** (type safety)
- **vite** (build tool)
- **axios** (HTTP client)
- **zustand** (state management)
- **tailwindcss** (styling)
- **react-router-dom** (routing)

## 🔐 Security

- HTTPS-only in production
- CORS properly configured
- Input validation on all forms
- Secure camera permission handling
- No sensitive data in localStorage

## 📈 Performance

- Lazy loading components
- Image compression (JPEG quality 0.8)
- Canvas frame throttling (30 FPS max)
- IndexedDB for caching
- Service worker caching

## 🚦 Status

- [x] Camera component
- [x] Detection visualization
- [x] Inventory display
- [x] Recommendations UI
- [ ] Offline mode (in progress)
- [ ] Mobile optimization (planned)
- [ ] PWA support (planned)

## 📚 Component Documentation

Each component has JSDoc comments and TypeScript types. Example:

```typescript
/**
 * Displays live camera feed with detection overlay
 * @param {CameraProps} props - Component props
 * @returns {JSX.Element}
 */
export const CameraFeed: React.FC<CameraProps> = ({ onFrame, resolution })
```

## 🛠️ Development Scripts

```bash
npm run dev          # Start dev server
npm run build        # Build production
npm run preview      # Preview build
npm run test         # Run tests
npm run lint         # Lint code
npm run type-check   # TypeScript check
```

## 📝 Environment Variables

```
VITE_API_BASE_URL        # Backend API URL
VITE_API_TIMEOUT         # Request timeout (ms)
VITE_ENABLE_OFFLINE      # Enable offline mode
VITE_LOG_LEVEL           # Log level (debug/info/warn/error)
VITE_MAX_IMAGE_SIZE      # Max image size (bytes)
VITE_CAMERA_RESOLUTION   # Default resolution (WIDTHxHEIGHT)
```

## 📞 Support

See main project README for contact information.
