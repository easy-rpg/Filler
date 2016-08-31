<h1>RPG Filler</h1>
<p>
	Programa para automatizar a criação de personagens do RPG D&D 3.5
</p>
<p>
	O RPG Filler é um conjunto de scripts feitos em Python, então para poder executá-lo é necessário ter o Python instalado no seu computador. Caso não tenha acesse <a href="https://www.python.org/">https://www.python.org/</a> para baixar
</p>
<h2>Como utilizar</h2>
<ul>
	<li>
		<h4>Download</h4>
		<p>
			Realize o download zip desse reposítorio e extraia-o em qualquer pasta de seu computador
		</p>
	</li>
	<li>
		<h4>Executar</h4>
		<p>
			Dentro da pasta extraída, há um arquivo chamado "RPGFiller.py". Este é o arquivo 'executável'
		</p>
		<ul>
			<li>
				<h4>Windows</h4>
				<p>
					Abra um terminal na pasta extraída e execute o comando "python RPGFiller.py"
				</p>
				<ul>
					<li>
						<h5>Erro: "python não é reconhecido como um comando interno"</h5>
						<p>
							Caso ocorra esse erro ao executar o comando "python RPGFiller.py", dê uma olhada nesse <a href="http://stackoverflow.com/questions/7054424/python-not-recognised-as-a-command">fórum</a>
						</p>
					</li>
				</ul>
			</li>
			<li>
				<h4>Linux</h4>
				<p>
					Abra um terminal na pasta extraída e execute o comando "./RPGFiller.py" ou "python RPGFiller.py"
				</p>
			</li>
		</ul>
	</li>
	<li>
		<h4>Informações sobre o RPG Filler</h4>
		<p>
			O RPG Filler automatiza a criação de um personagem de D&D 3.5 calculando automaticamente o BBA, life e testes de resistência com base nas classes inseridas no personagem. 
			As classes disponíveis são:
		</p>
		<ul>
			<li>Bárbaro</li>
			<li>Bardo</li>
			<li>Clérigo</li>
			<li>Druida</li>
			<li>Guerreiro</li>
			<li>Ladino</li>
			<li>Mago</li>
			<li>Monge</li>
			<li>Paladino</li>
			<li>Ranger</li>
		</ul>
	</li>
</ul>
<h2>DEV's</h2>
<ul>
	<li>
		<h3>Classes Implementadas</h3>
		<ul>
			<li>
				<b>BBA</b>: classes que implementam os valores da BBA boa (de guerreiros e etc) e da BBA ruim (de magos e etc). Servem apenas para armazenar tais valores e não são instânciadas.
			</li>
			<li>
				<b>Class</b>: classe "Ser Superior" abstrata que será herdada pelas classes descritas abaixo. 
				<ul>
					<li>
						<b>Bárbaro</b>: 
					</li>
					<li>
						<b>Bardo</b>: 
					</li>
					<li>
						<b>Clérigo</b>: 
					</li>
					<li>
						<b>Druida</b>: 
					</li>
					<li>
						<b>Guerreiro</b>: 
					</li>
					<li>
						<b>Ladino</b>: 
					</li>
					<li>
						<b>Mago</b>: 
					</li>
					<li>
						<b>Monge</b>: 
					</li>
					<li>
						<b>Paladino</b>: 
					</li>
					<li>
						<b>Ranger</b>: 
					</li>
				</ul>
			</li>
			<li>
				<b>Personagem</b>: 
			</li>
			<li>
				<b>Resist</b>: 
			</li>
			<li>
				<b>Situacao</b>: 
			</li>
			<li>
				<b>Writer</b>: 
			</li>
			<li>
				<b>Application</b>: 
			</li>
			<li>
				<b>MenuBar</b>: 
			</li>
		</ul>
	</li>
	<li>
		<h3>Persistência de dados</h3>
		<p>
			A persistência foi feita atrávez de arquivos em formato JSON, localizados dentro da pasta "personagens"
		</p>
	</li>
</ul>







