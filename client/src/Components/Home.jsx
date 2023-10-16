
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
          <p>Ready to embark on a culinary adventure without leaving your home?
             Download DishDishes now, available on both iOS and Android. Deliciousness awaits! Get started and enjoy the convenience of food delivery like never before.

            </p>
            <button className='btn' onClick={ handlenavigate}>Get Started</button>
        </div>
      </section>
       
      <section className="about" id="about">
        <div className="row">
          <div className="col50">
            <h2 className='titleText'><span>A</span>bout Us</h2>
            <p>At DishDishes, we're more than just a food delivery app;
               we're your trusted culinary companion on a mission to redefine your dining experience. Our journey began with a simple idea - to connect you with your favorite local eateries and introduce you to exciting new flavors, 
              all from the comfort of your own home.<br></br>DishDishes was founded by a group of passionate foodies who shared a common dream: to make great food accessible to everyone. What started as a local food delivery service in Kenya has since grown into a nationwide platform, 
              connecting food lovers with a world of culinary delights. .</p>
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