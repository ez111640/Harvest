import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import "./PinDetail.css"
import { useEffect } from "react";
import { getAllPins } from "../../../store/pinsReducer";

export const PinDetail = () => {
	const allPins = useSelector((state) => state.pinsReducer.pins)
	const dispatch = useDispatch()
	const allPinArray = Object.values(allPins)
	const pinId = useParams().pinId
	const thisPin = allPinArray.find((pin) => pin.id == pinId)
	let domain;

	if (thisPin) {
		const url = thisPin?.link
		const splitUrl = url.split("/")
		if (splitUrl[0] === "https:") {
			domain = splitUrl[2].split(".")[0]
		}
	}

	useEffect(() => {
		dispatch(getAllPins())
	}, [dispatch])

	if (!allPinArray.length) return null
	if(!thisPin) return null
	return (
		<div id="pin-detail-container">
			<div id="pin-detail-left"><img src={thisPin?.url}></img></div>
			<div id="pin-detail-right">
				<div></div>
				<div className="pin-details pin-detail-title">{thisPin.title}</div>
				<div className="pin-details pin-detail-description">{thisPin.description}</div>
				<div className="pin-details">{domain}</div>
				<div>
					<div>Comments</div>
					<div>No comments yet</div>
				</div>
				<div>
					<div>What do you think?</div>
					<div></div>
				</div>
			</div>

		</div>
	);
}
