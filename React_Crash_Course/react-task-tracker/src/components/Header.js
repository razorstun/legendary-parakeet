import PropTypes from 'prop-types'
import Button from './Button'

const Header = ({ title }) => {
    const onClick = () => {
        console.log('Click')
    }

    return (
        <header className='header'>
            {/* <h1 style={{ color: 'red', backgroundColor: 'black' }}>{title}</h1> */}
            <h1>{title}</h1>
            <Button text='Add' onClick={onClick}/>
        </header>
    )
}

Header.defaultProps = {
    title: 'Task tracker',
}

Header.propTypes = {
    title: PropTypes.string
}

export default Header
