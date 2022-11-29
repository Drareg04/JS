const { SlashCommandBuilder } = require('discord.js');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('ping')
		.setDescription('Replies with Pong!'),
	async execute(interaction) {
    await messages.create({
      "channel_id": `${context.params.event.channel_id}`,
      "content": "",
      "tts": false,
      "components": [
        {
          "type": 1,
          "components": [
            {
              "custom_id": `row_0_select_0`,
              "placeholder": `Chose an option`,
              "options": [
                {
                  "label": `Rock`,
                  "emoji": {
                    "id": rock,
                    "name": `🗿`
                  },
                  "default": false
                },
                {
                  "label": `Fire`,
                  "emoji": {
                    "id": fire,
                    "name": `🔥`
                  },
                  "default": false
                },
                {
                  "label": `Scissors`,
                  "emoji": {
                    "id": scissors,
                    "name": `✂`
                  },
                  "default": false
                },
                {
                  "label": `Snake `,
                  "emoji": {
                    "id": snake,
                    "name": `🐍`
                  },
                  "default": false
                },
                {
                  "label": `Human`,
                  "emoji": {
                    "id": human,
                    "name": `🧍`
                  },
                  "default": false
                },
                {
                  "label": `Tree`,
                  "emoji": {
                    "id": tree,
                    "name": `🌲`
                  },
                  "default": false
                },
                {
                  "label": `Wolf`,
                  "emoji": {
                    "id": wolf,
                    "name": `🐺`
                  },
                  "default": false
                },
                {
                  "label": `Sponge`,
                  "emoji": {
                    "id": sponge,
                    "name": `🧽`
                  },
                  "default": false
                },
                {
                  "label": `Paper`,
                  "emoji": {
                    "id": paper,
                    "name": `📄`
                  },
                  "default": false
                },
                {
                  "label": `Air`,
                  "emoji": {
                    "id": air,
                    "name": `💨`
                  },
                  "default": false
                },
                {
                  "label": `Water`,
                  "emoji": {
                    "id": water,
                    "name": `💦`
                  },
                  "default": false
                },
                {
                  "label": `Dragon`,
                  "emoji": {
                    "id": dragon,
                    "name": `🐉`
                  },
                  "default": false
                },
                {
                  "label": `Devil`,
                  "emoji": {
                    "id": devil,
                    "name": `😈`
                  },
                  "default": false
                },
                {
                  "label": `Ligthning`,
                  "emoji": {
                    "id": ligthning,
                    "name": `⚡`
                  },
                  "default": false
                },
                {
                  "label": `Gun`,
                  "emoji": {
                    "id": gun,
                    "name": `🔫`
                  },
                  "default": false
                }
              ],
              "min_values": 1,
              "max_values": 1,
              "type": 3
            }
          ]
        }
      ],
      "embeds": [
        {
          "type": "rich",
          "title": `Ultra Rock Paper Scissors`,
          "description": "",
          "color": 0x00FFFF,
          "image": {
            "url": `https://cdn.discordapp.com/attachments/888329272366862386/1043099100670865418/unknown.png`,
            "height": 0,
            "width": 0
          }
        }
      ]
    })
    await message.send()
  }
};
