import "./PinCard.css"
import { NavLink } from "react-router-dom"


export const PinCard = (pin) => {
    const thisPin = pin.pin
    return (
        <div className="pin-photo">
            <NavLink to={`/pins/${thisPin.id}`}>
                <img src={thisPin.url}></img>
            </NavLink>
        </div>
    )
}
