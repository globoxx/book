import './App.css';
import { HashRouter as Router, Routes, Route} from 'react-router-dom'
import Home from './pages/Home'
import Layout from './pages/Layout'

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/Layout" element={<Layout />} />
      </Routes>
    </Router>
  );
}

export default App;