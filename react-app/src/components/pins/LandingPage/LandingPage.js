import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { getAllPins } from "../../../store/pinsReducer"
import "./LandingPage.css"
import { PinCard } from "../PinCard/PinCard"

export const LandingPage = () => {
    const allPins = useSelector((state) => state.pinsReducer.pins)
    const dispatch = useDispatch()
    let allPinArray = []
    if (allPins) {
        allPinArray = Object.values(allPins)
    }
    useEffect(() => {
        dispatch(getAllPins())
    }, [dispatch])

    if (!allPinArray.length) return null
    return (
        <div id="all-pins">
            {allPinArray.map((pin) => (
                <div>
                    <PinCard pin={pin} />
                </div>
            ))}
        </div>
    )
}
