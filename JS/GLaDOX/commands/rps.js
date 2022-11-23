const { SlashCommandBuilder, EmbedBuilder, ActionRowBuilder, SelectMenuBuilder  } = require('discord.js');
module.exports = {
	data: new SlashCommandBuilder()
		.setName('rps')
		.setDescription('Ultra Rock Paper Scissors'),

  
  async execute(interaction) {
  const rps = new EmbedBuilder()
    .setColor(0x0099FF)
    .setTitle('Ultra rock paper scissors')
    .setDescription('Chose an option')
    .setImage('https://cdn.discordapp.com/attachments/888329272366862386/1043099100670865418/unknown.png')
    .setTimestamp()
  interaction.reply({embeds: [rps], components: [row] });
    },
};
