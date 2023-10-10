
import '../index.css'
import { useNavigate } from 'react-router-dom'
import foodImage from '../images/img1.jpg'


const Home = () => {
  
  const navigate = useNavigate()
  const handlenavigate = () => {
    navigate('/register')
  }

  return (
    <div>
      <section className="banner" id="banner">
        <div className="content">
          <h2>Always Choose Good</h2>
          <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. 
            Exercitationem aut, ex ipsam eum voluptates adipisci deserunt iusto? 
            Reprehenderit repudiandae natus odio odit fugiat maiores impedit, 
            debitis atque, veniam laudantium sed.</p>
            <button className='btn' onClick={ handlenavigate}>Get Started</button>
        </div>
      </section>
       
      <section className="about" id="about">
        <div className="row">
          <div className="col50">
            <h2 className='titleText'><span>A</span>bout Us</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. 
               Molestiae recusandae obcaecati ipsa cum aperiam, voluptas at animi ab inventore illo omnis quod,
               culpa dolores, magnam numquam odit architecto? Doloremque, aperiam.<br></br>Lorem ipsum dolor sit amet consectetur adipisicing elit. 
               Quia maxime laboriosam laborum nam reprehenderit officiis quae?
                Accusantium perferendis, voluptates fugit temporibus facilis quidem consectetur rem quos similique consequatur laborum suscipit.</p>
          </div>
        

        <div className="col50">
          <div className="imgBx">
            <img src={foodImage}/>
          </div>
        </div>
        </div>
            
      </section>
    
    </div>
  )
}

export default Home