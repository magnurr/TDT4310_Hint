let JSO = require('./DJT.json');



const data = JSO.map(tweet => {
    if ("device" in tweet) {
        const { id, text, isRetweet, date } = tweet;
        const ID = BigInt(id).toString()
        const timeStamp = new Date(date).getTime()
        return { ID, timeStamp, text, isRetweet }
    } else {
        let { date, text, isRetweet, id } = tweet;
        const ID = id
        const timeStamp = date
        isRetweet = isRetweet ? "t" : "f"
        return { ID, timeStamp, text, isRetweet }
    }
    return {}
})

const main = async () => {
    const fs = require('fs').promises;

    try {
        await fs.writeFile('realDonaldTrump.json', JSON.stringify(data)); // need to be in an async function
    } catch (error) {
        console.log(error)
    }
}



main()