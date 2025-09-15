# Tattvam Frontend

Modern React.js frontend for the Tattvam e-commerce platform, featuring a beautiful UI for authentic Indian products.

## 🌟 Features

- **React 18**: Latest React with hooks and concurrent features
- **Responsive Design**: Mobile-first approach with Tailwind CSS
- **Modern UI**: Clean, intuitive interface inspired by Indian aesthetics
- **State Management**: React Context for global state
- **Routing**: React Router for seamless navigation
- **API Integration**: Axios for backend communication
- **Notifications**: Toast notifications for user feedback
- **Search & Filter**: Advanced product search and filtering
- **Shopping Cart**: Persistent cart with real-time updates
- **Authentication**: Secure login/registration system

## 🎨 Design System

### Color Palette
- **Primary**: Orange (#f2730b) - Represents Indian saffron
- **Secondary**: Saffron (#f97316) - Traditional Indian color
- **Accent**: Yellow (#fbbf24) - Gold accents
- **Neutral**: Gray scale for text and backgrounds

### Typography
- **Font**: Inter - Modern, readable font
- **Headings**: Bold weights for emphasis
- **Body**: Regular weight for readability

### Components
- **Cards**: Rounded corners with subtle shadows
- **Buttons**: Primary, secondary, and ghost variants
- **Forms**: Clean input fields with validation
- **Navigation**: Sticky header with search functionality

## 🚀 Getting Started

### Prerequisites
- Node.js 18+
- npm or yarn

### Installation

1. **Navigate to frontend directory**
   ```bash
   cd frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start development server**
   ```bash
   npm start
   ```

4. **Open browser**
   Navigate to http://localhost:3000

### Using Docker

```bash
docker build -t tattvam-frontend .
docker run -p 3000:80 tattvam-frontend
```

## 📁 Project Structure

```
src/
├── components/          # Reusable UI components
│   ├── Navbar.js       # Navigation component
│   ├── ProductCard.js  # Product display card
│   └── ProtectedRoute.js # Route protection
├── pages/              # Page components
│   ├── Home.js         # Landing page
│   ├── Products.js     # Product listing
│   ├── ProductDetail.js # Product details
│   ├── Cart.js         # Shopping cart
│   ├── Login.js        # Login page
│   ├── Register.js     # Registration page
│   ├── Profile.js      # User profile
│   └── Orders.js       # Order history
├── contexts/           # React contexts
│   ├── AuthContext.js  # Authentication state
│   └── CartContext.js  # Shopping cart state
├── services/           # API services
│   └── api.js          # Axios configuration
├── App.js              # Main App component
└── index.js            # Application entry point
```

## 🎯 Key Components

### Navbar
- Logo and branding
- Search functionality
- Cart icon with item count
- User authentication status
- Mobile-responsive menu

### ProductCard
- Product image with hover effects
- Product information display
- Rating stars
- Add to cart button
- Price formatting

### Cart
- Item listing with quantities
- Quantity adjustment
- Remove items
- Order summary
- Checkout functionality

### Authentication
- Login form with validation
- Registration form
- Password visibility toggle
- Social login buttons (UI only)
- Protected routes

## 🔧 Configuration

### Environment Variables
```bash
REACT_APP_API_URL=http://localhost:8000  # Backend API URL
```

### Tailwind Configuration
Custom colors and fonts are configured in `tailwind.config.js`:
- Primary and saffron color palettes
- Inter font family
- Custom spacing and sizing

## 🎨 Styling

### Tailwind CSS Classes
The application uses utility-first CSS with Tailwind:

```jsx
// Example component styling
<div className="bg-white rounded-lg shadow-md hover:shadow-xl transition-shadow duration-300">
  <h2 className="text-2xl font-bold text-gray-900 mb-4">
    Product Title
  </h2>
  <p className="text-gray-600">
    Product description
  </p>
</div>
```

### Responsive Design
- **Mobile**: Single column layout
- **Tablet**: Two column layout
- **Desktop**: Multi-column layout with sidebar

### Dark Mode Support
Ready for dark mode implementation with CSS variables.

## 🔄 State Management

### AuthContext
Manages user authentication state:
- Login/logout functionality
- Token management
- User profile data
- Protected route access

### CartContext
Manages shopping cart state:
- Add/remove items
- Quantity updates
- Cart persistence
- Total calculations

## 🌐 API Integration

### Axios Configuration
```javascript
// services/api.js
const api = axios.create({
  baseURL: process.env.REACT_APP_API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});
```

### Request/Response Interceptors
- Automatic token attachment
- Error handling
- Loading states

## 🧪 Testing

### Run Tests
```bash
npm test
```

### Test Coverage
```bash
npm test -- --coverage
```

### Testing Tools
- Jest for unit testing
- React Testing Library for component testing
- Axios mock for API testing

## 📱 Mobile Responsiveness

### Breakpoints
- **sm**: 640px and up
- **md**: 768px and up
- **lg**: 1024px and up
- **xl**: 1280px and up

### Mobile Features
- Touch-friendly buttons
- Swipe gestures
- Mobile-optimized forms
- Responsive images

## 🚀 Build and Deployment

### Production Build
```bash
npm run build
```

### Build Optimization
- Code splitting
- Tree shaking
- Minification
- Asset optimization

### Deployment
The build output is optimized for:
- Static hosting (Netlify, Vercel)
- CDN deployment
- Docker containers
- Traditional web servers

## 🔧 Development Tools

### Available Scripts
```bash
npm start          # Start development server
npm run build      # Build for production
npm test           # Run tests
npm run eject      # Eject from Create React App
```

### Code Quality
- ESLint for code linting
- Prettier for code formatting
- Husky for git hooks (future)

## 🎨 UI/UX Features

### Loading States
- Skeleton loaders
- Spinner animations
- Progressive loading

### Error Handling
- Error boundaries
- Toast notifications
- Fallback UI components

### Accessibility
- ARIA labels
- Keyboard navigation
- Screen reader support
- Color contrast compliance

## 🔮 Future Enhancements

- [ ] Dark mode toggle
- [ ] PWA support
- [ ] Offline functionality
- [ ] Advanced animations
- [ ] Virtual scrolling for large lists
- [ ] Image lazy loading
- [ ] Search suggestions
- [ ] Product comparison
- [ ] Wishlist functionality
- [ ] Social sharing
- [ ] Multi-language support
- [ ] Advanced filtering
- [ ] Product reviews
- [ ] Recommendation engine

## 📊 Performance

### Optimization Techniques
- React.memo for component memoization
- useMemo and useCallback for expensive operations
- Code splitting with React.lazy
- Image optimization
- Bundle size optimization

### Metrics
- Lighthouse score: 90+
- First Contentful Paint: < 2s
- Largest Contentful Paint: < 3s
- Cumulative Layout Shift: < 0.1

## 🐛 Troubleshooting

### Common Issues

1. **API Connection Issues**
   - Check REACT_APP_API_URL environment variable
   - Verify backend server is running
   - Check CORS configuration

2. **Build Issues**
   - Clear node_modules and reinstall
   - Check Node.js version compatibility
   - Verify all dependencies are installed

3. **Styling Issues**
   - Ensure Tailwind CSS is properly configured
   - Check for CSS conflicts
   - Verify responsive breakpoints

## 📞 Support

For frontend support:
- Create an issue in the repository
- Email: frontend-support@tattvam.com
- Check the documentation at /docs

---

**Built with ❤️ using React and modern web technologies**