import { useEffect } from "react"
import { getAllPins, getBoardPins } from "../../../../store/pinsReducer"
import { useDispatch, useSelector } from "react-redux"
import "./BoardCard.css"
import { getUserBoards } from "../../../../store/boardsReducer"

export const BoardCard = ({ boardId }) => {
    const dispatch = useDispatch()
    const boardPins = useSelector((state) => (state.pinsReducer.boardPins[boardId]))
    const boards = useSelector((state) => state.boardsReducer)


    useEffect(() => {
        dispatch(getAllPins())
        dispatch(getUserBoards())
        dispatch(getBoardPins(boardId))
    }, [dispatch])

    if (!boardPins) return null
    if (!boards) return null
    const boardPinArray = Object.values(boardPins)
    const boardArray = Object.values(boards)

    const board = boardArray.find((board) => board.id == board.id)
    console.log(board)
    return (
        <div>
            <div className="board-cover-photo-div">
                <img className="board-cover-photo" src={boardPinArray[boardPinArray.length - 1].url}></img>
            </div>

        </div>
    )
}
