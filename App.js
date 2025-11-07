import Home from './pages/Home';
import Header from './pages/Header';
import NotFound from './pages/NotFound';
import{BrowserRouter, Routes,Route} from 'react-router-dom';
const App=()=>{
  return(
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/header' element={<Header />} />
        <Route path='*' element={<NotFound />} />
        
      </Routes>
    </BrowserRouter>
  )
}
export default App;
