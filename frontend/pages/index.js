import Head from 'next/head'
import Link from 'next/Link'
import Carousel from '../components/Carousel'
import Navbar from '../components/Navbar'

function Home() {
    return (

        <div>
            <Head>
                <meta charSet="utf-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0"></meta>
                <title>Portal A+zônia - Início</title>
            </Head>

            <Navbar />

            <div className='mt-3'>

                <div className='text-center'>
                    <h1 className='text-center'>Bem-vindo (a) ao <b>Portal A+zônia!</b></h1>
                    <hr></hr>
                    <p>O Portal A+zônia foi criado com o objetivo de ficar por dentro de índices de queimada dos munícipios da <b>Amazonia Legal</b>!</p>
                    <p >Este projeto faz parte da matéria <b><Link className='text-black' href='https://mds.lappis.rocks' target='_blank'>Métodos de Desenvolvimento de Sistemas</Link></b>.</p>
                    <hr></hr>
                </div>

                <div className='flex flex-col gap-5 rounded border p-4 card'>
                    <div className='grid grid-cols-3 gap-5 content card-body'>
                        <div className='flex flex-col items-center justify-end text-center'>
                            <Link target='_blank' href='https://github.com/fdiogo1'><img alt="Foto Diogo Ferreira" loading="lazy" width="100px" height="100px" decoding="async" data-nimg="1" className="rounded-circle" src='/images/diogo-ferreira.png'></img></Link>
                            <p className='text-black'><b>Diogo Ferreira</b></p>
                            <Link target='_blank' href='https://github.com/GuilhermeDavila'><img alt="Foto Diogo Ferreira" loading="lazy" width="100px" height="100px" decoding="async" data-nimg="1" className="rounded-circle" src='/images/guilherme-davila.jpeg'></img></Link>
                            <p className='text-black'><b>Guilherme Davila</b></p>
                            <Link target='_blank' href='https://github.com/GuilhermeOliveira1327'><img alt="Foto Diogo Ferreira" loading="lazy" width="100px" height="100px" decoding="async" data-nimg="1" className="rounded-circle" src='/images/guilherme-oliveira.jpeg'></img></Link>
                            <p className='text-black'><b>Guilherme Oliveira</b></p>
                            <Link target='_blank' href='https://github.com/bigkaio'><img alt="Foto Diogo Ferreira" loading="lazy" width="100px" height="100px" decoding="async" data-nimg="1" className="rounded-circle" src='/images/kaio-macedo.jpeg'></img></Link>
                            <p className='text-black'><b>Kaio Macedo</b></p>
                            <Link target='_blank' href='https://github.com/devwallyson'><img alt="Foto Diogo Ferreira" loading="lazy" width="100px" height="100px" decoding="async" data-nimg="1" className="rounded-circle" src='/images/wallyson-souza.jpeg'></img></Link>
                            <p className='text-black'><b>Wallyson Souza</b></p>
                            <Link target='_blank' href='https://github.com/renanpariiz'><img alt="Foto Diogo Ferreira" loading="lazy" width="100px" height="100px" decoding="async" data-nimg="1" className="rounded-circle" src='/images/renan-pariz.jpeg'></img></Link>
                            <p className='text-black'><b>Renan Pariz</b></p>
    
                        </div>
                    </div>      
                </div>

                <hr></hr>

                <div className="card" id='card1'>
                        <div className="card-body">
                            <h5 className="card-title">GitHub</h5>
                            <p className="card-text">Repositório onde se encontra o projeto.</p>
                            <Link href="https://github.com/unb-mds/2024-2-Amaiszonia" target='_blank' className="btn btn-primary">Clique para ir</Link>
                        </div>
                </div>
                <hr></hr>
                <div>
                    <h2>Compromissos ambientais</h2>
                </div>


            </div>

        </div>

    )
}

export default Home