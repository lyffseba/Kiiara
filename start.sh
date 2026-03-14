#!/bin/bash
# Start Kiiara locally for testing

echo "Starting Kiiara local development environment..."

# Start backend
source venv/bin/activate
echo "Starting ADK web server on port 8080..."
adk web backend --port 8080 > backend.log 2>&1 &
BACKEND_PID=$!

# Wait for backend to start
sleep 5

# Start frontend
cd frontend
echo "Starting frontend dev server on port 3000..."
npm run dev > ../frontend.log 2>&1 &
FRONTEND_PID=$!
cd ..

# Wait for frontend to start
sleep 5

# Check if servers are running
if curl -s http://localhost:8080 > /dev/null; then
    echo "✓ Backend running at http://localhost:8080"
    echo "  Voice interface (ADK UI): http://localhost:8080"
else
    echo "✗ Backend failed to start. Check backend.log"
fi

if curl -s http://localhost:3000 > /dev/null; then
    echo "✓ Frontend running at http://localhost:3000"
else
    echo "✗ Frontend failed to start. Check frontend.log"
fi

echo ""
echo "Kiiara is ready!"
echo "Open http://localhost:3000 in Chromium for the full experience."
echo "Voice interface is available at http://localhost:8080 (embedded in frontend)."
echo ""
echo "Press Ctrl+C to stop servers."

# Trap Ctrl+C to kill background processes
trap "kill $BACKEND_PID $FRONTEND_PID 2>/dev/null; echo 'Servers stopped.'; exit" INT

# Wait indefinitely
wait