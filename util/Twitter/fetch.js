require('dotenv').config()
const util = require('util');
const fs = require('fs').promises;

var Twitter = require('twitter');


const search_terms_tweets  = ["hei"]
const search_terms_people = ["BarackObama","realDonaldTrump"]

const client = new Twitter({
    consumer_key: process.env.TWITTER_API_KEY,
    consumer_secret: process.env.TWITTER_API_SECRET,
    access_token_key: process.env.TWITTER_ACCESS_TOKEN_KEY,
    access_token_secret: process.env.TWITTER_ACCESS_TOKEN_SECRET
  });


let clientGetPromise = function(endpoint,payload) {
    return new Promise((resolve, reject) => {
      client.get(endpoint, payload, (err,tweets,response) => {
        if (err) reject(err);
        else resolve(tweets);
      });
    });
  };
  
const fetcher = async (loop,terms,api_end_point,search_type,return_val,inital_max_id,storage,storage_term) => {
    for (const term of terms) {
    let max_id = inital_max_id;
    for (const index of [...Array(loop).keys()]){
      let tweets = await clientGetPromise(api_end_point, {[search_type]: term, count:100,max_id})
      const cursor =  return_val == null ? 'nan': return_val
      if (return_val == null) tweets = {[cursor]:tweets}
      max_id = Math.min(...tweets[cursor].map((tweet) => tweet.id))-1
      console.log(max_id)
      if (index == 0) storage[storage_term][term] = tweets;
      else storage[storage_term][term][cursor].push(...tweets[cursor])
    }
  }
}

const output = {users:{},terms:{}}

async function main() {
  const fetchAmount = 1000;
  const loops = fetchAmount/100;

  let max_id = Number.MAX_SAFE_INTEGER
  //await fetcher(loops,search_terms_tweets,'search/tweets','q','statuses',max_id,output,'terms')
  await fetcher(loops,search_terms_people,'statuses/user_timeline','screen_name',null,max_id,output,'users')
      Object.keys(output.users).forEach(async (key)=>{
        await fs.writeFile(`tweets/users/${key}.json`, JSON.stringify(output.users[key]));
    } )
    Object.keys(output.terms).forEach(async (key)=>{
        await fs.writeFile(`tweets/terms/${key}.json`, JSON.stringify(output.terms[key]));
    } )
  }



main()
