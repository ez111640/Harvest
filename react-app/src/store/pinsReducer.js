export const LOAD_PINS = 'pinsReducer/loadPins'
export const LOAD_BOARD_PINS = 'pinsReducer/loadBoardPins'
export const ADD_PIN = "/pinsReducer/addNewPin"
export const UPDATE_PIN = "/pinsReducer/putPin"

export const loadPins = (pins) => ({
    type: LOAD_PINS,
    pins
})

export const loadBoardPins = (boardPins) => ({
    type: LOAD_BOARD_PINS,
    boardPins
})

export const addNewPin = (pin) => ({
    type: ADD_PIN,
    pin
})

export const putPin = (pin) => ({
    type: UPDATE_PIN,
    pin
})

export const getAllPins = (query) => async (dispatch) => {
    let res;
    if (query) {
        res = await fetch(`/api/pins?${query}`)
    } else {
        res = await fetch(`/api/pins`)
    }
    if (res.ok) {
        const allPins = await res.json();
        const allPinArray = Object.values(allPins)

        dispatch(loadPins(allPinArray))
    } else {
        const errors = await res.json();
        return errors;
    }
}

export const getBoardPins = (id) => async (dispatch) => {
    let res;
    if (id) {
        res = await fetch(`/api/boards/${id}/pins`)
        if (res.ok) {
            const boardPins = await res.json();
            const boardPinArray = Object.values(boardPins)
            boardPinArray.map(
                async (btp) => {
                    res = await fetch(`/api/pins/${btp.pinId}`)
                    btp.pin = await res.json()
                })
            dispatch(loadBoardPins(boardPinArray))
        } else {
            const errors = await res.json();
            return errors;
        }
    }
}

export const updatePinThunk = (pin) => async (dispatch) => {

    const res = await fetch(`/api/pins/$pin.id}`, {
        method: 'PUT',
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(pin)
    })
    const oldPin = await res.json()
    oldPin.review = pin.review
    oldPin.stars = pin.stars
    oldPin.likes = pin.likes

    dispatch(putPin(oldPin))
}

export const addPinThunk = (pin) => async (dispatch) => {

    try {
        const res = await fetch(`/api/pins`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(pin)
        });


        const pinResponse = await res.json()
        if (res.ok) {
            dispatch(addNewPin(pinResponse))
        } else {
            const errors = await res.json();
            return errors;
        }
    } catch (error) {
        const errors = await error.json();
        return errors;
    }
}


const initialState = {};
export const pinsReducer = (state = initialState, action) => {
    let newState = { ...state }
    switch (action.type) {
        case LOAD_PINS:
            return { ...state, pins: { ...action.pins }, boardPins: { ...state.boardPins } }
        case LOAD_BOARD_PINS:
            action.boardPins.forEach((boardPin) => {
                state.boardPins[boardPin.boardId] = boardPin
            })
            return { ...state, pins: { ...state.pins } }
        case ADD_PIN:
            newState = { ...state, pins: { ...state.pins }, boardPins: { ...state.boardPins } }
            newState.pins[action.pin.id] = action.pin
            return newState
        default:
            return state;
    }
}
