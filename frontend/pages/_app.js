import '../styles/global.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import { useEffect } from 'react';


function MyApp({ Component, pageProps }) {
    useEffect(() => {
        // Carregue o JavaScript do Bootstrap apenas no cliente
        if (typeof window !== 'undefined') {
          import('bootstrap/dist/js/bootstrap.bundle.min.js');
        }
      }, []);
    
      return <Component {...pageProps} />;
}

export default MyApp;