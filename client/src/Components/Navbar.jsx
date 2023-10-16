import React from 'react'
import { NavLink ,useLocation} from 'react-router-dom'
import {useEffect} from 'react'

const Navbar = () => {
  const location = useLocation()

  if(location.pathname === '/account'){
    return null
  }else if (location.pathname.startsWith('/restaurant')){
    return null
  }

  useEffect(() => {
    // Add the scroll event listener within the useEffect hook
    window.addEventListener("scroll", function () {
      const header = document.querySelector('header');
      header.classList.toggle("sticky", window.scrollY > 0);
    });

    // remove the event listener when the component unmounts
    return () => {
      window.removeEventListener("scroll", function () {
        const header = document.querySelector('header');
        header.classList.toggle("sticky", window.scrollY > 0);
      });
    };
  }, []);


  return (
    <div>
        <header>

        
<NavLink to='/' className="logo">Food <span>.</span></NavLink>

<ul className="navigation active">
  <li><NavLink to="/" className="navs">Home</NavLink></li>
  <li><a className="navs" href='#about'>About</a></li>
  <li><NavLink to="/register" className="navs">SignUp</NavLink></li>
  <li><NavLink to="/login" className="navs">SignIn</NavLink></li>
</ul>
</header>
    </div>
  )
}

export default Navbar