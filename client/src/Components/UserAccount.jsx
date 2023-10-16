import React, { useEffect, useState } from 'react';
import {useNavigate, Link, useParams} from 'react-router-dom';
import foodImage from '../images/burger.jpeg';
import friedchicken from '../images/chickenbucket.jpeg';
import fries from '../images/fries5.webp'
import pasta from '../images/pasta2.webp'
import biriani from '../images/biriani.jpeg'
import burger from '../images/burder6.jpeg'

const UserAccount = () => {
  const [userData, setuserData] =useState({})
  const [restaurants, setRestaurant] = useState({}); 
  const [loading, setLoading] = useState(true);

  

  const navigate = useNavigate()
  

  useEffect(() => {
    // fetch user data using their access token
    const accessToken = localStorage.getItem('accessToken');
    const fetchdata =async () =>{
      try{
        const response = await fetch("https://flask-apidelivery.onrender.com/users/account",{
          method:'GET',
          headers:{
            'Authorization':`Bearer ${accessToken}`,
          },
        });
        if (response.status === 200){
          const data = await response.json();
          setuserData(data);
        }else if(response.status === 401){
          navigate('/login')
        } else {
          console.log('Error:', response.status);
        }
      }catch(error){
        console.error('Error:', error)
    } finally {
      setLoading(false); // Set loading state to false when done
    }
  };

    fetchdata();

    // fetch restaurants
    
    const fetchRestaurants = async () => {
      try {
        const response = await fetch('https://flask-apidelivery.onrender.com/restaurants/dashboard', {
          method: 'GET',
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
        });
        if (response.status === 200) {
          const data = await response.json();
          setRestaurant(data);
        } else {
          console.log('Error:', response.status);
        }
      } catch (error) {
        console.error('Error:', error);
      }
    };

    fetchRestaurants();
  },[]);

  const handleLogout = async () => {
    // Send a request to log the user out on the server
    const accessToken = localStorage.getItem('accessToken');
    try {
      const response = await fetch('https://flask-apidelivery.onrender.com/auth/logout', {
        method: 'POST',
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      });

      if (response.status === 200) {
        // Clear the access token and redirect to the login page
        localStorage.removeItem('accessToken');
        navigate('/login');
      } else {
        console.log('Error:', response.status);
      }
    } catch (error) {
      console.error('Error:', error);
    }
  }

  return (
     <div className='containerss'>
      <nav className='navbar'>
        <div className='logo'>
          <p>Food<span>.</span></p>
        </div>

        <div className="user-info">
          <div className="user-welcome">
            <i className="fas fa-user"></i>
            <p className='align'>welcome:{userData.username}</p>
            <button className='btn8' onClick={handleLogout}>Log out</button>
          </div>
        </div>
      </nav>
      <h2 className="col mt-5 text-center">Welcome To DishDishes!!</h2>
      <div className="col text-center mb-0 text-gray">Welcome to DishDishes delicious universe. Everything from our Big on Breakfast, Perfected Drinks, Decadent to your Generous Big Meals Right here at your fingertips. ORDER NOW.
      </div>
      <div className="container menu-parent-div text-center">
        {/* Display restaurant cards */}
        <div className="row mt-5">
          {Array.isArray(restaurants) &&
          restaurants.map((restaurant, index) => (
            <div className="col-lg-6 mb-4" key={restaurant.id}>
              <div className="card menu-card bg-light" style={{ width: "30rem" }}>
                {/* Add a link to the restaurant's details page */}
                <Link to={`/restaurant/${restaurant.id}`}>
                <img
                  src={
                    index === 0
                      ? foodImage
                      : index === 1
                      ? friedchicken
                      : index === 2
                      ? fries
                      : index === 3// Provide a default image here
                      ? pasta
                      : index === 4
                      ? biriani
                      : index === 5
                      ? burger
                      : index === 6
                  }
                  className="card-img-top"
                  alt={restaurant.name}
                />
                </Link>
                <div className="card-body">
                  <p>{restaurant.name}</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
    
  )
}

export default UserAccount;