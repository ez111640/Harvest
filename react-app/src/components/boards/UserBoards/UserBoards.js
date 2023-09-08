import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux"
import { getUserBoards } from "../../../store/boardsReducer"
import { BoardCard } from "./BoardCard/BoardCard";
import { getAllPins } from "../../../store/pinsReducer";
import { Link } from 'react-router-dom'
import CreatePinModal from "../../pins/CreatePinModal"
import "./UserBoards.css"
import { useModal } from "../../../context/modal";
import OpenModalButton from "../../OpenModalButton";



export const UserBoards = () => {
    const user = useSelector((state) => state.session.user)
    const userBoards = useSelector((state) => state.boardsReducer)
    const dispatch = useDispatch();
    const firstLetter = user.username[0]

    // const { closeModal } = useModal()

    window.onbeforeunload = function () {
        window.setTimeout(function () {
            window.location = '/';
        }, 0);
        window.onbeforeunload = null; // necessary to prevent infinite loop, that kills your browser
    }

    useEffect(() => {
        dispatch(getUserBoards())
        dispatch(getAllPins())
    }, [dispatch])

    // const handleSubmit = (e) => {
    //     e.preventDefault();
    // }


    const userBoardArray = Object.values(userBoards)

    if (!userBoardArray.length) return null
    return (
        <div>
            <div className="profile-header">
                <div className="profile-div-left">
                    <div className="user-spot">
                        {firstLetter}
                    </div>
                    <div className="profile-div-left-buttons">
                        <OpenModalButton
                            buttonText="Create a Pin"
                            modalComponent={<CreatePinModal />}
                        />
                        <div>Create a Pin</div>
                    </div>
                </div>
                <div className="profile-div-right"></div>
            </div>
            <div className="user-board-listing">
                {userBoardArray.map(
                    (board) => (
                        <div>
                            <Link to={`/boards/${board.id}`}><BoardCard boardId={board.id} /></Link>
                            <div className="board-name">{board.name}</div>
                        </div>
                    )

                )}
            </div>
        </div>
    )
}
