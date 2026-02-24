function Frame({ description, etiquettes, bgi }) {
    return(
        <div className='update-info' style={{backgroundImage: `url(${bgi})`}}>
            <div className='etiquette-container'>
                {etiquettes.map((etiquette, index) => (<p key={index} className={`etiquette ${etiquette}`}>{etiquette.toUpperCase()}</p>))}
            </div>
            <p className='description'>{description}</p>
        </div>
    )
}

export default Frame