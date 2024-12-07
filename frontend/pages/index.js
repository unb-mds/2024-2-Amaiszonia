import Head from 'next/head'
import Link from 'next/Link'
import 'bootstrap/dist/css/bootstrap.min.css'

function Home() {
    return (

        <div className="d-flex align-items=center py-4 h-100">
            <Head>
                <meta charSet="utf-8"/>
                <meta name="viewport" content="width=device-width, initial-scale=1.0"></meta>
                <title>Portal A+zônia - Início</title>
            </Head>
            <main className="container mt-5">
                <img src="logo2.png" id="logo-image" className="rounded mx-auto d-block mb-4" height="105" width="180"/>
                <h1 className="text-center text-white">Portal A+zônia</h1>
                <p className='text-center text-white fw-bold'>O <b>Portal A+zonia</b> é um projeto da matéria 
                    Métodos de Desenvolvimento de Software 2024-2, ministrada na <b>Universidade de Brasília</b>.</p>
                <h3 className="text-center text-white">Métodos de Desenvolvimento de Software</h3>
                <p className='text-center text-white'><b>Universidade de Brasília</b></p>
                <ul className="text-center text-white">
                    <li className='mb-0'><Link href='https://github.com/unb-mds/2024-2-Squad10' className='text-white fw-bold' target='_blank'>GitHub</Link></li>
                    <li className='mb-0 text-primary'><Link href='https://unb-mds.github.io/2024-2-Squad10' className='text-white fw-bold' target='_blank'>GitPage</Link></li>
                    <li className='mb-0 text-primary'><Link href='/dados' className='text-white fw-bold' target='_blank'>Dados</Link></li>
                </ul>
            </main>
        </div>

    )
}

export default Home;