const { Client, GatewayIntentBits, EmbedBuilder, ActionRowBuilder, ButtonBuilder, ButtonStyle } = require('discord.js');
const fs = require('fs');

const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.GuildMembers,
    GatewayIntentBits.MessageContent,
  ]
});

const prefix = '!';
const ownerID = '1322285991805059112'; // Seu ID aqui

// Banco de dados simples em JSON
let db = {};
let dbDaily = {};
let dbWarn = {};

const dbFile = './db.json';
const dbDailyFile = './db_daily.json';
const dbWarnFile = './db_warn.json';

// Carregar DBs
if (fs.existsSync(dbFile)) db = JSON.parse(fs.readFileSync(dbFile));
if (fs.existsSync(dbDailyFile)) dbDaily = JSON.parse(fs.readFileSync(dbDailyFile));
if (fs.existsSync(dbWarnFile)) dbWarn = JSON.parse(fs.readFileSync(dbWarnFile));

// Salvar DBs
function saveDB() { fs.writeFileSync(dbFile, JSON.stringify(db, null, 2)); }
function saveDBDaily() { fs.writeFileSync(dbDailyFile, JSON.stringify(dbDaily, null, 2)); }
function saveDBWarn() { fs.writeFileSync(dbWarnFile, JSON.stringify(dbWarn, null, 2)); }

client.once('ready', () => {
  console.clear();
  console.log('🌑 Eclipse Bot v6.0 Online!');
});

client.on('messageCreate', async (message) => {
  if (message.author.bot || !message.guild) return;
  if (!message.content.startsWith(prefix)) return;

  const userId = message.author.id;
  if (!db[userId]) db[userId] = { xp: 0, coins: 0, warns: 0, inventory: [] };
  if (!dbWarn[userId]) dbWarn[userId] = 0;

  const args = message.content.slice(prefix.length).trim().split(/ +/);
  const cmd = args.shift().toLowerCase();

  // Anti-link (não para admins)
  if (message.content.includes('http') && !message.member.permissions.has('ManageMessages')) {
    await message.delete();
    return message.channel.send(`⛔ Link proibido, ${message.author}!`);
  }

  // Comandos
  if (cmd === 'ping') {
    return message.reply(`🏓 Pong! Latência: ${client.ws.ping}ms`);
  }

  if (cmd === 'créditos') {
    const embed = new EmbedBuilder()
      .setColor('Blue')
      .setTitle('🌑 Eclipse Bot')
      .setDescription('Desenvolvido por Recex Supreme')
      .addFields(
        { name: 'Criador', value: `<@${ownerID}>` },
        { name: 'Versão', value: '6.0' }
      );
    const row = new ActionRowBuilder().addComponents(
      new ButtonBuilder()
        .setLabel('GitHub Recex')
        .setStyle(ButtonStyle.Link)
        .setURL('https://github.com/RecexSupreme')
    );
    return message.channel.send({ embeds: [embed], components: [row] });
  }

  if (cmd === 'perfil') {
    const userData = db[userId];
    const embed = new EmbedBuilder()
      .setColor('Gold')
      .setTitle(`Perfil de ${message.author.username}`)
      .addFields(
        { name: 'XP', value: `${userData.xp}`, inline: true },
        { name: 'Moedas', value: `${userData.coins}`, inline: true },
        { name: 'Advertências', value: `${dbWarn[userId]}`, inline: true }
      );
    return message.channel.send({ embeds: [embed] });
  }

  if (cmd === 'daily') {
    const now = Date.now();
    if (!dbDaily[userId]) dbDaily[userId] = 0;

    if (now - dbDaily[userId] < 86400000) {
      const restante = 86400000 - (now - dbDaily[userId]);
      const hrs = Math.floor(restante / 3600000);
      const mins = Math.floor((restante % 3600000) / 60000);
      return message.reply(`⏳ Você já pegou seu daily. Tente novamente em ${hrs}h ${mins}m.`);
    }

    dbDaily[userId] = now;
    db[userId].coins += 100;
    saveDB();
    saveDBDaily();
    return message.reply('📆 Você recebeu 100 moedas diárias!');
  }

  if (cmd === 'avatar') {
    const user = message.mentions.users.first() || message.author;
    return message.channel.send(user.displayAvatarURL({ dynamic: true, size: 512 }));
  }

  if (cmd === 'limpar') {
    if (!message.member.permissions.has('ManageMessages')) {
      return message.reply('⛔ Você não tem permissão para usar esse comando.');
    }
    const amount = parseInt(args[0]);
    if (!amount || amount < 1 || amount > 100) {
      return message.reply('Digite um número válido entre 1 e 100.');
    }
    await message.channel.bulkDelete(amount + 1);
    return message.channel.send(`🧹 ${amount} mensagens limpas.`).then(msg => {
      setTimeout(() => msg.delete(), 5000);
    });
  }

  if (cmd === 'warn') {
    if (!message.member.permissions.has('KickMembers')) {
      return message.reply('⛔ Você não tem permissão para usar esse comando.');
    }
    const member = message.mentions.members.first();
    if (!member) return message.reply('Mencione um membro para advertir.');
    const motivo = args.slice(1).join(' ') || 'Sem motivo';

    if (!dbWarn[member.id]) dbWarn[member.id] = 0;
    dbWarn[member.id]++;
    saveDBWarn();

    return message.channel.send(`⚠️ ${member.user.tag} foi advertido. Motivo: ${motivo}`);
  }

  // XP e moedas por mensagem
  db[userId].xp += 10;
  db[userId].coins += 2;
  saveDB();
});

client.login('SEU_TOKEN_AQUI');
