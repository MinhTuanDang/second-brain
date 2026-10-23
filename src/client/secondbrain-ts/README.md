<div align="center">
    <a href="https://secondbrain.io">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://assets.secondbrain.io/secondbrain-dark.svg">
      <img alt="Shows the Second Brain logo" src="https://assets.secondbrain.io/secondbrain-light.svg" width="424">
    </picture>
  </a>
  <p><strong>User Profile-Based Memory for GenAI Apps</strong></p>
  <p>
    <a href="https://www.npmjs.com/package/@secondbrain/secondbrain">
      <img src="https://img.shields.io/npm/v/@secondbrain/secondbrain.svg?logo=npm&&logoColor=fff&style=flat&colorA=2C2C2C&colorB=28CF8D">
    </a>
    <a href="https://jsr.io/@secondbrain/secondbrain">
      <img src="https://img.shields.io/jsr/v/@secondbrain/secondbrain.svg?logo=jsr&&logoColor=fff&style=flat&colorA=2C2C2C&colorB=28CF8D" />
    </a>
    <a href="https://npmcharts.com/compare/@secondbrain/secondbrain?minimal=true">
      <img src="https://img.shields.io/npm/dm/@secondbrain/secondbrain.svg?logo=typescript&&logoColor=fff&style=flat&colorA=2C2C2C&colorB=28CF8D" />
    </a>
    <a href="https://github.com/secondbrain-labs/secondbrain/actions/workflows/publish.yaml">
      <img src="https://github.com/secondbrain-labs/secondbrain/actions/workflows/publish.yaml/badge.svg">
    </a>
  </p>
</div>

# Second Brain TypeScript and JavaScript API Library
This library provides convenient access to the Second Brain REST API from TypeScript or JavaScript.


## Installation

```sh
npm install @secondbrain/secondbrain
```

### Installation from JSR

```sh
deno add jsr:@secondbrain/secondbrain
npx jsr add @secondbrain/secondbrain
```


## Usage

The code below shows how to get started using the completions API.

<!-- prettier-ignore -->
```js
import { SecondBrainClient, Blob, BlobType } from '@secondbrain/secondbrain';

const client = new SecondBrainClient(process.env['SECONDBRAIN_PROJECT_URL'], process.env['SECONDBRAIN_API_KEY'])

const main = async () => {
    const ping = await client.ping()
    console.log('Ping: ', ping)

    const config = await client.getConfig()
    console.log('Config: ', config)

    const updateConfig = await client.updateConfig('a: 1')
    console.log('Update config: ', updateConfig)

    let userId = await client.addUser()
    console.log('Add user: ', userId)

    userId = await client.updateUser(userId, { name: 'John Doe' })
    console.log('Updated user id: ', userId)

    let user = await client.getUser(userId)
    console.log('User: ', user)

    const blobId = await user.insert(Blob.parse({
        type: BlobType.Enum.chat,
        messages: [{
            role: 'user',
            content: 'Hello, how are you? my name is John Doe'
        }]
    }))
    console.log('Insert blob: ', blobId)

    const blob = await user.get(blobId)
    console.log('Blob: ', blob)

    const flushSuc = await user.flush(BlobType.Enum.chat)
    console.log('Flush success: ', flushSuc)

    const blobs = await user.getAll(BlobType.Enum.chat)
    console.log('Blobs: ', blobs)

    user = await client.getOrCreateUser(userId)
    console.log('Get or create user: ', user)

    const addProfileSuc = await user.addProfile("Content", "Topic1", "SubTopic1")
    console.log('Add profile success: ', addProfileSuc)

    const profiles = await user.profile(2000)
    console.log('Profiles: ', profiles)

    const updateProfileSuc = await user.updateProfile(profiles[0].id, "New Content", "New Topic", "New SubTopic")
    console.log('Update profile success: ', updateProfileSuc)

    const deleteProfileSuc = await user.deleteProfile(profiles[0].id)
    console.log('Delete profile success: ', deleteProfileSuc)

    const event = await user.event(10, 1000)
    console.log('Event: ', event)

    const updateEventSuc = await user.updateEvent(event[0].id, {
        "id": event[0].id,
        "event_data": {
            "profile_delta": [
                {
                    "content": "New Event Content",
                    "attributes": {
                        "topic": "interest",
                        "sub_topic": "foods"
                    }
                }
            ]
        },
        created_at: new Date(),
        updated_at: new Date()
    })
    console.log('Update event success: ', updateEventSuc)

    const deleteEventSuc = await user.deleteEvent(event[0].id)
    console.log('Delete event success: ', deleteEventSuc)

    const context = await user.context(2000, 1000)
    console.log('Context: ', context)

    const isDel = await client.deleteUser(userId)
    console.log('Delete user success: ', isDel)
}

main()
```

## Support

Join the community for support and discussions:

-  [Join our Discord](https://discord.gg/YdgwU4d9NB) 👻 

-  [Follow us on Twitter](https://x.com/secondbrain_io) 𝕏 

Or Just [email us](mailto:contact@secondbrain.io) ❤️


## Contributors

This project exists thanks to all the people who contribute.

And thank you to all our backers! 🙏

<a href="https://github.com/secondbrain-labs/secondbrain/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=secondbrain-labs/secondbrain" />
</a>


## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](https://github.com/secondbrain-labs/secondbrain/blob/main/LICENSE) file for details.