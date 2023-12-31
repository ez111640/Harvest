import React, {useState } from "react";
import { NavLink, useHistory } from "react-router-dom";
import { useSelector } from "react-redux";
import ProfileButton from "./ProfileButton";
import "./navigation.css";

function Navigation({ isLoaded }) {
  // const dispatch = useDispatch()
  const sessionUser = useSelector((state) => state.session.user);
  const [searchInput, setSearchInput] = useState("")
  const history = useHistory()
  // let searchProducts = []



  const handleChange = (e) => {
    e.preventDefault();
    setSearchInput(e.target.value);
    if (searchInput.length > 0) {
    }
  }

  const onClick = (e) => {
    e.preventDefault();
    if (searchInput) history.push(`/products/search/${searchInput}`)
  }

  const onEnter = () => {
    if (searchInput) history.push(`/products/search/${searchInput}`)
  }

  return (
    <div className="main-nav-bar">
      <div>
        <NavLink exact to="/">
          <img src="https://i.ibb.co/rbztcLh/HAR-1.png" className="harvest-logo" alt="HAR-1" border="0"></img>
        </NavLink>
      </div>
      <div className="search-bar">
        <input
          className="search-bar-input"
          type="text"
          placeholder="Search"
          onChange={handleChange}
          value={searchInput}
          onKeyDown={(e) => (e.key === "Enter" ? onEnter() : false)}
        />
        <button className="hide-that-button" onClick={onClick} ><i className="fa-solid fa-magnifying-glass" ></i></button>
      </div>
      <div>
          <ProfileButton className="nav-link profile-button" user={sessionUser} />


      </div>
    </div>
  );
}

export default Navigation;
