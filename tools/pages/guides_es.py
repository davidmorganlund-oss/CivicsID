"""Guías en español (noviembre de 2026). Mismos datos y fuentes que las guías en inglés.
Las páginas quedan en site/es/guides/<slug>.html con el mismo slug que la versión en inglés."""
G = {}

PRM = "https://www.ag.idaho.gov/content/uploads/2026/07/PublicRecordsLaw.pdf"
OML = "https://www.ag.idaho.gov/content/uploads/2026/07/OpenMeeting.pdf"

G["speak-at-a-public-meeting"] = dict(
    cat="Local", title="Cómo hablar en una reunión pública local",
    lede="Los concejos municipales, los comisionados del condado, las juntas escolares y los distritos de carreteras toman la mayoría de las decisiones que usted siente en el día a día. Esto es lo que la ley de Idaho le garantiza, lo que no, y cómo aprovechar dos minutos.",
    body="""
  <h2>Lo que la ley de Idaho le garantiza</h2>
  <p>La Ley de Reuniones Abiertas de Idaho (Código de Idaho, Título 74, Capítulo 2) se aplica a los órganos de gobierno de condados, ciudades, distritos escolares, distritos especiales y juntas y comisiones estatales.</p>
  <ul>
    <li><strong>Puede asistir.</strong> Las reuniones de un órgano de gobierno están abiertas al público, y las decisiones deben tomarse en público (§ 74-203).</li>
    <li><strong>Recibe aviso.</strong> Una reunión ordinaria requiere por lo menos cinco días calendario de aviso y una agenda publicada con 48 horas de anticipación. Una reunión especial requiere 24 horas de aviso de ambas cosas. Un órgano que se reúne con un horario fijo puede publicar ese horario una vez al año, pero cada reunión todavía necesita su agenda con 48 horas de anticipación (§ 74-204).</li>
    <li><strong>La agenda tiene que ser real.</strong> En general, el órgano solo puede decidir lo que está en la agenda, y los asuntos que se votarán deben marcarse como "action items" (puntos de acción). Agregar algo tarde requiere una votación y una razón de por qué no se pudo incluir antes.</li>
    <li><strong>Las sesiones a puerta cerrada son limitadas.</strong> Solo se permiten por razones que la ley enumera, como contratar personal, la disciplina de un empleado específico, comprar terrenos o demandas pendientes. Requieren un voto nominal de dos tercios que indique la razón, y no se puede tomar ninguna decisión final a puerta cerrada (§ 74-206).</li>
    <li><strong>Hay actas.</strong> Las actas escritas deben registrar quién estuvo presente, cada moción y cada votación, y estar disponibles al público (§ 74-205).</li>
    <li><strong>Puede grabar.</strong> Puede grabar audio o video de una reunión abierta, y no pueden expulsarle de la reunión por hacerlo (§ 74-203(6)).</li>
  </ul>

  <h2>Lo que no le garantiza</h2>
  <p><strong>La Ley de Reuniones Abiertas le da el derecho a observar, no el derecho a hablar.</strong> Un órgano no está obligado a recibir comentarios del público en una reunión ordinaria. La mayoría de los concejos municipales y juntas escolares lo hacen por decisión propia, según sus propias reglas. Muchas comisiones de condado lo hacen con menos frecuencia.</p>
  <p><strong>Las audiencias públicas son diferentes.</strong> Cuando una ley exige una audiencia, el órgano debe dejar que la gente testifique. Eso incluye el presupuesto anual, la mayoría de las decisiones de zonificación y uso de suelo, y muchos aumentos de tarifas. Si quiere asegurarse de ser escuchado, una audiencia pública es el lugar.</p>

  <h2>Antes de la reunión</h2>
  <ol>
    <li><strong>Encuentre la reunión.</strong> El <a href="../">calendario</a> muestra lo que viene cerca de usted.</li>
    <li><strong>Lea la agenda.</strong> Busque el asunto que le interesa y anote su número o título, y si es un punto de acción o una audiencia pública. Casi todas las agendas están en inglés; puede pedirle ayuda al secretario (clerk).</li>
    <li><strong>Averigüe cómo recibe comentarios ese órgano.</strong> Cada uno pone sus propias reglas: si hay que inscribirse antes o en la puerta, cuánto tiempo le dan y si puede hablar por teléfono o video. Llame al secretario si el sitio web no lo dice.</li>
    <li><strong>Pida un intérprete con tiempo.</strong> Muchas ciudades y condados ofrecen interpretación si se pide con anticipación. Pregunte al secretario unos días antes.</li>
    <li><strong>Si no hay período de comentarios,</strong> envíe un correo a los miembros antes de la reunión, o pregunte al secretario cómo poner un asunto en una agenda futura.</li>
  </ol>

  <h2>Qué decir</h2>
  <p>El tiempo suele ser corto, a menudo dos o tres minutos, así que escríbalo y mida el tiempo.</p>
  <ol>
    <li><strong>Quién es usted.</strong> Su nombre y que vive, trabaja o tiene un negocio en la comunidad. En una audiencia, por lo general le pedirán su dirección para el registro.</li>
    <li><strong>De qué habla.</strong> Nombre el asunto de la agenda.</li>
    <li><strong>Qué quiere que hagan.</strong> Votar a favor, en contra, cambiar algo específico o aplazarlo.</li>
    <li><strong>Una razón.</strong> Un ejemplo personal breve convence más que una lista de argumentos.</li>
    <li><strong>Repita su petición y dé las gracias.</strong></li>
  </ol>

  <h2>Después de hablar</h2>
  <ul>
    <li><strong>No espere una respuesta en el momento.</strong> La mayoría de los órganos escuchan y no responden durante los comentarios.</li>
    <li><strong>Haga seguimiento por escrito.</strong> Envíe por correo los mismos puntos, más lo que no alcanzó a decir.</li>
    <li><strong>Esté atento a la votación.</strong> La decisión puede tomarse en una reunión posterior.</li>
  </ul>

  <h2>Si un órgano no cumple las reglas</h2>
  <p>Una decisión tomada en una reunión que no cumplió la Ley de Reuniones Abiertas se puede anular. Primero avise al órgano por escrito: entonces tiene 14 días para responder y puede corregir el problema volviendo a tomar la decisión en público. Las quejas sobre órganos locales van al fiscal del condado (county prosecuting attorney), y las quejas sobre órganos estatales van al Fiscal General (Attorney General). Una persona afectada por la decisión también puede ir a la corte, pero solo dentro de 30 días a partir de la decisión. Vea <a href="open-meeting-law.html">la Ley de Reuniones Abiertas de Idaho</a> para más detalles.</p>
""",
    sources=[("https://legislature.idaho.gov/statutesrules/idstat/Title74/T74CH2/", "Código de Idaho, Título 74, Capítulo 2: Ley de Reuniones Abiertas (en inglés)"),
             (OML, "Manual de la Ley de Reuniones Abiertas de Idaho, julio de 2026, Fiscal General (en inglés)")])

G["open-meeting-law"] = dict(
    cat="Local", title="La Ley de Reuniones Abiertas de Idaho: qué exige",
    lede="Cuando un concejo municipal, una comisión del condado, una junta escolar u otro órgano público se reúne para decidir o discutir asuntos públicos, la ley de Idaho dice que el público tiene derecho a verlo. Esto es lo que garantiza, lo que no, y qué puede hacer cuando un órgano no cumple.",
    body="""
  <h2>A quién se aplica</h2>
  <p>La ley se aplica a los órganos de gobierno de agencias estatales y locales: concejos municipales, comisiones de condado, juntas escolares, juntas de bibliotecas y de distritos de carreteras, y las comisiones y comités que toman decisiones o hacen recomendaciones (Código de Idaho §§ 74-202(4)&ndash;(5)). No se aplica a los tribunales, a un funcionario que actúa solo, ni a grupos privados como organizaciones sin fines de lucro o asociaciones de propietarios.</p>
  <p>Una <strong>reunión</strong> es cualquier encuentro de un quórum para tomar una decisión o deliberar sobre ella, sea formal, informal o social (§ 74-202(6)). Los miembros no pueden evitar la ley reuniéndose en grupos más pequeños o pasando opiniones por medio de otra persona, y los intercambios por correo o mensajes de texto entre un quórum también pueden contar. Deliberar incluye intercambiar información u opiniones sobre una decisión pendiente. El consejo del Fiscal General a los órganos públicos: "cuando tenga dudas, abra la reunión" ("when in doubt, open the meeting").</p>

  <h2>Aviso y agendas</h2>
  <ul>
    <li><strong>Reuniones ordinarias:</strong> por lo menos 5 días calendario de aviso de la reunión y 48 horas de aviso de la agenda (§ 74-204(1)). Los órganos que se reúnen al menos una vez al mes pueden publicar su calendario anual en su lugar.</li>
    <li><strong>Reuniones especiales:</strong> por lo menos 24 horas de aviso de la reunión y de la agenda (§ 74-204(2)). Las verdaderas emergencias son una excepción, y el órgano debe explicar la emergencia al inicio de la reunión.</li>
    <li>Los avisos se publican en la oficina de la agencia y en su sitio web o redes sociales, si los tiene.</li>
    <li>Las agendas deben indicar los temas específicos, y todo lo que se vaya a votar debe marcarse como <strong>punto de acción</strong> ("action item") (§ 74-204(4)). Agregar un asunto tarde requiere una moción que explique por qué no estaba en la agenda, y la decisión final sobre un asunto agregado tarde por lo general requiere una emergencia.</li>
  </ul>

  <h2>Sesiones a puerta cerrada ("executive sessions")</h2>
  <p>Un órgano solo puede cerrar parte de una reunión por las razones que enumera el § 74-206(1), y se interpretan de manera estricta. Incluyen:</p>
  <ul>
    <li>Contratar, evaluar o disciplinar a un empleado específico (no las políticas generales de personal).</li>
    <li>Comprar una propiedad que no sea de una agencia pública.</li>
    <li>Hablar con su abogado sobre un litigio pendiente o probable.</li>
    <li>Registros que están exentos de divulgación, negociaciones laborales y algunas otras razones.</li>
  </ul>
  <p>Para cerrar la sesión, el órgano debe votar con una <strong>mayoría de dos tercios en votación nominal</strong>, citando la razón específica, y una vez adentro no puede pasar a otros temas. <strong>No se puede tomar ninguna decisión final a puerta cerrada</strong> (§ 74-206). La votación tiene que ser en público.</p>

  <h2>Sus derechos</h2>
  <ul>
    <li><strong>Asistir.</strong> Se permiten reglas para mantener el orden, pero no reglas que hagan imposible asistir.</li>
    <li><strong>Grabar.</strong> Puede grabar reuniones abiertas en audio, video o fotos, y no pueden expulsarle de la reunión por hacerlo (§ 74-203(6)).</li>
    <li><strong>Actas.</strong> Cada reunión requiere actas escritas con los presentes, las mociones y los resultados de las votaciones, disponibles al público en un plazo razonable (§ 74-205). No se permiten votaciones secretas (§ 74-203(1)).</li>
    <li><strong>Un lugar físico.</strong> Se permiten reuniones remotas, pero por lo menos un miembro o el director de la agencia debe estar en el lugar anunciado para que el público pueda asistir (§ 74-203(5)).</li>
  </ul>
  <p>Lo que la ley <strong>no</strong> le da es el derecho a hablar. Vea <a href="speak-at-a-public-meeting.html">cómo hablar en una reunión pública local</a>.</p>

  <h2>Cuando un órgano no cumple la ley</h2>
  <ol>
    <li><strong>Avise por escrito.</strong> El órgano tiene 14 días para responder públicamente y, si está de acuerdo, otros 14 días para corregirlo declarando nulas las decisiones de esa reunión (§ 74-208(7)).</li>
    <li><strong>Presente una queja.</strong> El fiscal del condado (county prosecuting attorney) hace cumplir la ley para los órganos locales; el Fiscal General (Attorney General), para las agencias estatales (§ 74-208(5)). Los miembros que violan la ley a sabiendas pueden recibir multas personales: hasta $1,500, o $2,500 si lo repiten dentro de un año, y hasta $250 por participar en una reunión que no cumple la ley (§ 74-208(2)&ndash;(4)).</li>
    <li><strong>Vaya a la corte.</strong> Cualquier persona afectada por una violación puede demandar en la división de magistrados de la corte de distrito (magistrate court) del condado donde se reúne el órgano. Una demanda para anular una decisión debe presentarse dentro de <strong>30 días</strong> a partir de la decisión; otras demandas, dentro de 180 días a partir de la violación (§ 74-208(6)). Las demandas privadas pueden anular decisiones, pero no pueden obtener multas ni indemnización por daños.</li>
  </ol>
  <p>El Manual de la Ley de Reuniones Abiertas del Fiscal General, gratuito, tiene la ley completa y respuestas a decenas de preguntas comunes. El enlace está abajo (en inglés).</p>
""",
    sources=[(OML, "Manual de la Ley de Reuniones Abiertas de Idaho, julio de 2026, Fiscal General (en inglés)"),
             ("https://www.ag.idaho.gov/office-resources/manuals/", "Página de manuales del Fiscal General (en inglés)"),
             ("https://legislature.idaho.gov/statutesrules/idstat/Title74/T74CH2/", "Código de Idaho, Título 74, Capítulo 2 (en inglés)")])

G["public-records-requests"] = dict(
    cat="Local", title="Cómo pedir registros públicos en Idaho",
    lede="Correos electrónicos, contratos, presupuestos, informes policiales, paquetes de reuniones: casi todo lo que escriben los gobiernos de Idaho pertenece al público. Así se piden, cuánto cuestan, cuándo deben responder y qué hacer si le dicen que no.",
    body="""
  <h2>Qué puede pedir</h2>
  <p>Un registro público es cualquier documento sobre asuntos públicos que una agencia estatal o local prepara, posee, usa o guarda, en cualquier forma: papel, correo electrónico, mensajes de texto, hojas de cálculo, fotos o grabaciones (Código de Idaho § 74-101(13)). La ley cubre las agencias estatales, la Legislatura y los registros administrativos de las cortes, y todas las agencias locales: condados, ciudades, distritos escolares y distritos especiales (§ 74-101).</p>
  <p>Cualquier persona puede pedirlos (§ 74-102(1)). En general, la agencia no puede preguntarle para qué los quiere. Tampoco tiene que crear un documento que no existe, así que pida documentos, no respuestas a preguntas.</p>

  <h2>Cómo hacer la solicitud</h2>
  <ol>
    <li><strong>Busque al encargado de registros</strong> ("records custodian"). Cada agencia debe nombrar por lo menos uno (§ 74-102(16)). Busque "public records request" en el sitio web de la agencia; muchas tienen un formulario en línea. Envíe su solicitud al encargado: una solicitud enviada a la persona equivocada puede no poner en marcha el plazo (§ 74-103(1)).</li>
    <li><strong>Hágalo por escrito.</strong> El correo electrónico sirve (§ 74-102(4)). Diga claramente que es una solicitud de registros públicos. Puede escribir en español, pero la respuesta y los documentos probablemente estarán en inglés.</li>
    <li><strong>Describa los documentos con detalle,</strong> con un rango de fechas. "Los correos entre el administrador de la ciudad y el director de parques sobre el parque de Main Street, del 1 de enero al 31 de marzo de 2026" recibe una respuesta más rápida y más barata que "todo sobre el parque".</li>
    <li><strong>Incluya sus datos de contacto.</strong> La ley pide su nombre, dirección postal, correo y teléfono, y una declaración escrita de si vive en Idaho (§ 74-102(4)). La residencia cambia los plazos y costos. Significa haber vivido en Idaho por lo menos 30 días seguidos (§ 74-101(15)).</li>
    <li><strong>Diga cómo los quiere.</strong> Si los documentos existen en forma electrónica, puede pedir copias electrónicas (§ 74-102(15)). También puede pedir revisarlos en persona en lugar de comprar copias.</li>
  </ol>
  <div class="callout">
    <p><strong>Una solicitud sencilla (en inglés, para enviar a la agencia)</strong></p>
    <p>"This is a public records request under Idaho Code &sect; 74-102. Please provide electronic copies of [describa los documentos] from [fecha de inicio] to [fecha final]. I am / am not an Idaho resident. My contact information: [nombre, dirección, correo, teléfono]. If any part of this request is denied, please cite the specific exemption and release the rest of the record with the exempt parts redacted."</p>
  </div>

  <h2>Plazos</h2>
  <ul>
    <li><strong>Residentes de Idaho:</strong> la agencia tiene <strong>3 días hábiles</strong> para aceptar o denegar. Si necesita más tiempo para encontrar o copiar los documentos, debe avisarle por escrito y entregarlos dentro de <strong>10 días hábiles</strong> (§ 74-103(2)).</li>
    <li><strong>No residentes:</strong> 21 días, que pueden extenderse a 35 (§ 74-103(2)).</li>
    <li>Si pasa el plazo sin respuesta, la solicitud se considera denegada (§ 74-103(3)), y usted puede ir a la corte (vea abajo).</li>
  </ul>

  <h2>Costo</h2>
  <ul>
    <li><strong>Para residentes de Idaho, las primeras dos horas de trabajo y las primeras 100 páginas son gratis</strong> (§ 74-102(10)(a)). Después, la agencia puede cobrar el costo real de las copias y el tiempo del personal, a la tarifa del empleado con el sueldo más bajo que pueda hacer el trabajo.</li>
    <li>Los cobros deben estar detallados: costo por página, tarifa por hora y tiempo real. No se permite cobrar una sola cantidad global (§ 74-102(10)(h)).</li>
    <li>La agencia puede pedir un depósito antes de empezar, y debe devolverle lo que no use (§ 74-102(12)).</li>
    <li><strong>Exención de pago:</strong> la agencia debe eximirle del pago si los documentos ayudarán de manera importante al público a entender al gobierno, la solicitud no es principalmente para su beneficio personal y el costo le impediría obtenerlos (§ 74-102(10)(f)). Si es su caso, pida la exención en su solicitud.</li>
    <li>A los no residentes se les puede cobrar el costo real desde la primera página.</li>
  </ul>
  <p>Consejo: pedir copias electrónicas, o revisar los documentos en persona, por lo general cuesta menos que el papel.</p>

  <h2>Lo que pueden negar</h2>
  <p>La ley enumera excepciones, y las agencias deben aplicarlas de manera estricta. Cuando un documento tiene información exenta, la agencia debe tachar las partes exentas y entregarle el resto; no puede retener todo el documento solo por eso. Excepciones comunes:</p>
  <ul>
    <li><strong>Expedientes de personal,</strong> excepto que el puesto, el salario, el historial de empleo y el lugar de trabajo de cada empleado público son públicos (§ 74-106(1)).</li>
    <li><strong>Investigaciones policiales activas,</strong> en la medida en que entregarlas interferiría con ellas, pondría a alguien en peligro o invadiría la privacidad. Los datos básicos de un incidente y de un arresto siguen siendo públicos, y se puede ver más cuando la investigación ya no está activa (§ 74-124).</li>
    <li><strong>Datos de identificación personal,</strong> como los números de Seguro Social (§ 74-106).</li>
    <li><strong>Asesoría legal y documentos de litigios,</strong> secretos comerciales, y avalúos o estimaciones de ofertas antes de una compra o de la apertura de ofertas (§§ 74-104, 74-107).</li>
  </ul>
  <p>Los registros sobre usted mismo son diferentes: por lo general puede verlos aunque estarían exentos para otra persona, y puede pedirle a la agencia que los corrija (§ 74-113).</p>

  <h2>Si le dicen que no</h2>
  <ol>
    <li><strong>Revise la carta de denegación.</strong> Debe ser por escrito, citar la ley específica en la que se basa, decir si un abogado la revisó y explicarle su derecho a apelar (§ 74-103(4)&ndash;(5)).</li>
    <li><strong>Intente aclarar o reducir la solicitud.</strong> Muchas denegaciones y estimaciones de costo altas vienen de solicitudes demasiado amplias. Una llamada al encargado puede resolver mucho.</li>
    <li><strong>Vaya a la corte si es necesario.</strong> Puede presentar una petición en la corte de distrito del condado donde están los documentos dentro de <strong>180 días</strong> a partir de la denegación (§ 74-115(1)). No tiene que pasar antes por una apelación interna. La corte debe fijar una audiencia dentro de 28 días y puede revisar los documentos en privado para decidir. Si alguna de las partes actuó sin fundamento, la corte puede ordenar el pago de los honorarios de abogados (§ 74-116), y a un funcionario que niega de mala fe una solicitud legítima se le puede multar con hasta $1,000 (§ 74-117).</li>
  </ol>
  <p>La oficina del Fiscal General publica un manual gratuito con la ley completa, cartas de ejemplo y respuestas a preguntas comunes. Es la mejor referencia, y el enlace está abajo (en inglés).</p>
""",
    sources=[(PRM, "Manual de la Ley de Registros Públicos de Idaho, julio de 2026, Fiscal General (en inglés)"),
             ("https://www.ag.idaho.gov/office-resources/manuals/", "Página de manuales del Fiscal General (en inglés)"),
             ("https://legislature.idaho.gov/statutesrules/idstat/Title74/T74CH1/", "Código de Idaho, Título 74, Capítulo 1 (en inglés)")])

G["contact-your-representatives"] = dict(
    cat="Habilidades", title="Cómo comunicarse con quienes le representan",
    lede="Un mensaje corto y concreto de alguien que vive en el distrito sí se lee. Así se escoge la oficina correcta y esto es lo que debe decir el mensaje.",
    body="""
  <h2>Empiece con el nivel de gobierno correcto</h2>
  <p>La manera más rápida de no llegar a ningún lado es preguntarle a la oficina equivocada. Como guía general:</p>
  <ul>
    <li><strong>Ciudad:</strong> zonificación y permisos de construcción dentro de la ciudad, calles y banquetas, policía municipal, parques, agua y drenaje.</li>
    <li><strong>Condado:</strong> elecciones, avalúos de propiedad, el alguacil (sheriff) y la cárcel, el juzgado, y el uso de suelo fuera de la ciudad. Las licencias de manejo las da la oficina del alguacil del condado, y el registro de vehículos el tasador (assessor) del condado, según las reglas del estado.</li>
    <li><strong>Distrito de carreteras:</strong> en muchas partes de Idaho, un distrito electo aparte se encarga de los caminos locales. En el condado de Ada, el Distrito de Carreteras del Condado de Ada (Ada County Highway District, ACHD) maneja casi todas las calles locales, dentro y fuera de las ciudades.</li>
    <li><strong>Estado:</strong> financiamiento escolar, carreteras estatales, prisiones, Medicaid, parques estatales y las leyes estatales.</li>
    <li><strong>Federal:</strong> Seguro Social y Medicare, beneficios para veteranos, inmigración, pasaportes, impuestos federales, y los bosques nacionales y otras tierras federales que cubren gran parte de Idaho.</li>
  </ul>
  <p>¿No sabe quiénes le representan? Use <a href="../reps.html">la búsqueda por dirección</a>.</p>

  <h2>Qué poner en el mensaje</h2>
  <ol>
    <li><strong>Diga que vive en el distrito.</strong> Mencione su ciudad o pueblo.</li>
    <li><strong>Haga una sola petición.</strong> "Por favor vote a favor del proyecto de ley H 123" funciona mejor que una opinión general.</li>
    <li><strong>Dé su razón en pocas frases.</strong> Cómo le afecta a usted, a su familia o a su trabajo.</li>
    <li><strong>Que sea breve.</strong></li>
    <li><strong>Pida una respuesta</strong> e incluya cómo contactarle. Puede escribir en español; si lo necesita, diga que prefiere una respuesta en español.</li>
  </ol>

  <h2>Correo, teléfono o en persona</h2>
  <ul>
    <li><strong>El correo electrónico</strong> es lo más fácil de enviar y de dar seguimiento. La dirección de cada legislador está en el sitio web de la Legislatura.</li>
    <li><strong>Una llamada</strong> es rápida. Los legisladores de Idaho son de medio tiempo y la mayoría comparte personal, así que durante la sesión el Centro de Información Legislativa es la puerta de entrada: 208-332-1000, o 800-626-0471 sin costo.</li>
    <li><strong>Fuera de la sesión,</strong> los legisladores están en sus distritos. Muchos dan un número de casa o de celular y tienen reuniones comunitarias. A menudo es el mejor momento para ser escuchado.</li>
    <li><strong>En persona</strong> funciona mejor a nivel local. Vea <a href="speak-at-a-public-meeting.html">cómo hablar en una reunión pública local</a>.</li>
  </ul>

  <h2>Cuando necesita ayuda, no un voto</h2>
  <p>Si tiene un problema con una agencia de gobierno, las oficinas de los funcionarios electos a menudo pueden ayudar. Los miembros del Congreso tienen personal que atiende problemas con agencias federales. Los legisladores estatales pueden preguntarle a una agencia estatal por su caso, y la oficina del Gobernador también recibe solicitudes de constituyentes. Llame a la oficina y pida ayuda con un caso de constituyente ("constituent services").</p>
""",
    sources=[("https://legislature.idaho.gov/legislators/whosmylegislator/", "Who's My Legislator, Legislatura de Idaho (en inglés)"),
             ("https://legislature.idaho.gov/resources/committeetestimony/", "Cómo testificar ante comités legislativos (en inglés)"),
             ("https://legislature.idaho.gov/legislators/congressional-delegation/", "La delegación de Idaho en el Congreso, Legislatura de Idaho (en inglés)")])

G["local-government"] = dict(
    cat="Local", title="Cómo funciona el gobierno local",
    lede="Casi todo el gobierno con el que usted trata en el día a día es local. En Idaho eso significa su condado, su ciudad si vive en una, su distrito escolar y varios distritos especiales en los que quizás no sabe que vive.",
    body="""
  <h2>Condados</h2>
  <p>Idaho tiene 44 condados. Cada uno lo dirige una junta de tres comisionados del condado (county commissioners), que son a la vez quienes hacen las normas del condado y quienes lo administran. Los comisionados los elige todo el condado, pero cada uno debe vivir en un distrito de comisionado diferente.</p>
  <p>Los votantes también eligen a otros seis funcionarios del condado, y cada uno dirige su propia oficina:</p>
  <ul>
    <li><strong>Secretario (clerk):</strong> organiza las elecciones, guarda los registros de los comisionados y los expedientes de la corte, y registra las escrituras de propiedad.</li>
    <li><strong>Tasador (assessor):</strong> fija el valor de las propiedades para los impuestos y se encarga del registro de vehículos.</li>
    <li><strong>Tesorero (treasurer):</strong> cobra los impuestos a la propiedad.</li>
    <li><strong>Alguacil (sheriff):</strong> la policía fuera de las ciudades, la cárcel del condado y las licencias de manejo.</li>
    <li><strong>Fiscal del condado (prosecuting attorney):</strong> acusa los delitos ante la corte y es el abogado del condado.</li>
    <li><strong>Forense del condado (coroner):</strong> investiga las muertes.</li>
  </ul>
  <p>Si usted vive fuera de los límites de una ciudad, el condado es su gobierno local para la planeación, la zonificación y los permisos de construcción.</p>

  <h2>Ciudades</h2>
  <p>Idaho tiene unas 200 ciudades incorporadas, desde Boise hasta pueblos de unas cuantas docenas de personas. Casi todas usan la forma de alcalde y concejo: los votantes eligen a un alcalde, que dirige la ciudad en el día a día, y a un concejo municipal de cuatro o seis miembros, que aprueba las ordenanzas y el presupuesto. Unas pocas ciudades usan la forma de concejo y administrador, en la que el concejo contrata a un administrador profesional. Las elecciones municipales no son partidistas y se hacen en noviembre de los años impares.</p>

  <h2>Distritos escolares</h2>
  <p>Cada distrito escolar es su propio gobierno, dirigido por una junta escolar electa (board of trustees) que contrata al superintendente, fija las políticas y aprueba el presupuesto. Los miembros de la junta no reciben sueldo y se eligen en noviembre de los años impares. Las escuelas públicas chárter tienen sus propias juntas, que no son electas sino nombradas.</p>

  <h2>Distritos especiales</h2>
  <p>Idaho depende mucho de distritos que tienen un solo propósito, cada uno con su propia junta, su propio presupuesto y, muchas veces, su propia línea en su recibo de impuestos a la propiedad. Los más comunes:</p>
  <ul>
    <li><strong>Distritos de carreteras (highway districts),</strong> que construyen y mantienen los caminos locales en gran parte del estado.</li>
    <li><strong>Distritos de protección contra incendios</strong> y distritos de ambulancias.</li>
    <li><strong>Distritos de bibliotecas.</strong></li>
    <li><strong>Distritos de riego y de canales,</strong> que entregan el agua.</li>
    <li><strong>Distritos de cementerios, de recreación, de drenaje y de agua.</strong></li>
    <li><strong>Distritos de salud pública.</strong> Cada uno de los siete distritos de salud de Idaho atiende a varios condados y lo dirige una junta nombrada por los comisionados del condado.</li>
    <li><strong>Agencias de renovación urbana (urban renewal agencies),</strong> creadas por ciudades o condados para pagar la remodelación de una zona definida.</li>
  </ul>
  <p>Su recibo de impuestos a la propiedad muestra cada distrito que le cobra impuestos. Es la manera más rápida de saber en cuáles vive.</p>

  <section class="near-you" data-show="site,schools,districts" data-title="Sus gobiernos locales" aria-label="Sus gobiernos locales"></section>

  <h2>Dónde puede participar</h2>
  <ul>
    <li><strong>Reuniones.</strong> Todas estas juntas se reúnen en público y deben publicar su agenda con anticipación. Vea <a href="speak-at-a-public-meeting.html">cómo hablar en una reunión pública local</a>.</li>
    <li><strong>Audiencias sobre el presupuesto.</strong> Cada condado, ciudad y distrito debe hacer una audiencia pública sobre su presupuesto antes de aprobarlo, por lo general a fines del verano. Es la única reunión del año en la que todos los programas están sobre la mesa.</li>
    <li><strong>Elecciones.</strong> En los distritos pequeños, el resultado muchas veces se decide por unas cuantas docenas de votos, y a veces los puestos quedan vacíos porque nadie se postula. Vea <a href="running-for-office.html">cómo postularse a un cargo</a>.</li>
    <li><strong>Juntas por nombramiento.</strong> Las comisiones de planeación y zonificación, las juntas de bibliotecas y otras se llenan por nombramiento. Vea <a href="boards-and-commissions.html">cómo servir en una junta o comisión</a>.</li>
  </ul>
""",
    sources=[("https://archive.sos.idaho.gov/blue_book/blue_book_2025-2026.pdf", "The Blue Book of Idaho 2025-2026, sección sobre el gobierno de los condados, Secretaría de Estado de Idaho (en inglés)"),
             ("https://idcounties.org/wp-content/uploads/2025/10/Introduction-to-State-Local-Government.pdf", "Introducción al gobierno estatal y local, Asociación de Condados de Idaho (en inglés)"),
             ("https://legislature.idaho.gov/statutesrules/idstat/", "Código de Idaho: Título 31 (condados), Título 50 (ciudades), Título 33 (escuelas), Título 40 (carreteras), Legislatura de Idaho (en inglés)")])

G["your-neighborhood"] = dict(
    cat="Local", title="Lo que puede hacer en su vecindario",
    lede="No necesita un cargo para cambiar las cosas en su cuadra. Estas son maneras prácticas de lograr que arreglen los problemas y de organizar a la gente.",
    body="""
  <h2>Logre que arreglen un problema</h2>
  <ul>
    <li><strong>Repórtelo al lugar correcto.</strong> Los baches, las lámparas de la calle que no sirven y las señales que faltan le tocan a quien es dueño del camino: la ciudad, el departamento de caminos del condado o el distrito de carreteras local. En el condado de Ada casi siempre es el Ada County Highway District (el distrito de carreteras del condado de Ada). La basura tirada ilegalmente, la hierba crecida y los vehículos abandonados le tocan a la oficina de cumplimiento de códigos (code enforcement) de la ciudad o del condado.</li>
    <li><strong>Guarde el número de reporte.</strong> Si no pasa nada, haga seguimiento con ese número. Si después de eso sigue sin pasar nada, comuníquese con su concejal, su comisionado del condado o su comisionado del distrito de carreteras.</li>
    <li><strong>Invite a sus vecinos.</strong> Cinco hogares que reportan el mismo problema pesan más que uno.</li>
  </ul>

  <section class="near-you" data-show="site" data-title="Los sitios web de su ciudad y su condado" aria-label="Los sitios web de su ciudad y su condado"></section>

  <h2>Entérese de lo que se planea</h2>
  <ul>
    <li><strong>Esté atento a los avisos sobre uso de suelo.</strong> Los cambios de zonificación, los fraccionamientos y los permisos de uso especial requieren una audiencia pública. El aviso se publica, se envía por correo a los dueños de propiedades cercanas y, por lo general, se pone en la propiedad unas dos semanas antes. Si le llega uno, la fecha de la audiencia que aparece ahí es su oportunidad de testificar.</li>
    <li><strong>Pida registros.</strong> Bajo la Ley de Registros Públicos de Idaho, cualquier persona puede pedirle sus registros a una agencia estatal o local. Si usted vive en Idaho, la agencia debe aceptar o denegar la solicitud dentro de tres días hábiles, o avisarle que necesita hasta diez, y las primeras dos horas de trabajo del personal y las primeras 100 páginas son gratis. Desde un cambio a la ley en 2025, las personas que no viven en Idaho esperan hasta 21 días, que pueden extenderse a 35, y no reciben horas ni páginas gratis. Vea <a href="public-records-requests.html">cómo pedir registros públicos</a>.</li>
    <li><strong>Lea el plan integral (comprehensive plan).</strong> Cada ciudad y cada condado tiene uno, con un mapa del tipo de crecimiento que se planea en cada lugar. Las decisiones de zonificación deben seguirlo, así que es el mejor argumento que puede llevar a una audiencia.</li>
    <li><strong>Revise los planes de caminos.</strong> Los distritos de carreteras y el Idaho Transportation Department (el departamento de transporte del estado) publican listas de proyectos para varios años. Es más fácil lograr que un proyecto entre en la lista que agregarlo después.</li>
  </ul>

  <h2>Organícese</h2>
  <ul>
    <li><strong>Únase a una asociación de vecinos o forme una.</strong> Algunas ciudades registran oficialmente a las asociaciones de vecinos y les avisan de los proyectos cercanos.</li>
    <li><strong>Haga una fiesta de cuadra o una jornada de limpieza.</strong> Las ciudades muchas veces tienen permisos sencillos para cerrar una calle residencial, y algunas prestan materiales de limpieza.</li>
    <li><strong>Arme una cadena de llamadas o un chat de grupo.</strong> Parece poca cosa, pero es lo que permite que un vecindario se presente rápido cuando se acerca una decisión.</li>
  </ul>

  <h2>Llévelo a una reunión</h2>
  <p>Cuando un problema necesita una decisión, y no solo una reparación, llévelo a su concejo municipal, a los comisionados del condado o al distrito de carreteras. Vea <a href="speak-at-a-public-meeting.html">cómo hablar en una reunión pública local</a> y <a href="problem-to-policy.html">cómo convertir un problema personal en una propuesta de política pública</a>.</p>
""",
    sources=[("https://legislature.idaho.gov/statutesrules/idstat/Title74/T74CH1/SECT74-103/", "Código de Idaho § 74-103, respuesta a una solicitud de registros públicos, Legislatura de Idaho (en inglés)"),
             (PRM, "Manual de la Ley de Registros Públicos de Idaho, julio de 2026, Fiscal General (en inglés)"),
             ("https://legislature.idaho.gov/statutesrules/idstat/Title74/T74CH2/", "Código de Idaho, Título 74, Capítulo 2: Ley de Reuniones Abiertas, Legislatura de Idaho (en inglés)"),
             ("https://legislature.idaho.gov/statutesrules/idstat/", "Código de Idaho: Título 67, Capítulo 65, planeación local del uso de suelo, Legislatura de Idaho (en inglés)")])

G["local-ballot-measures"] = dict(
    cat="Local", title="Medidas locales en la boleta",
    lede="Los bonos, los impuestos (levies) y las iniciativas locales ponen las decisiones sobre impuestos y gastos directamente en manos de los votantes. Idaho pone algunos de los requisitos más altos del país para aprobarlos.",
    body="""
  <h2>Bonos: préstamos para proyectos grandes</h2>
  <p>Un bono permite que un distrito escolar, una ciudad, un condado u otro distrito pida dinero prestado para algo grande, como una escuela o una estación de bomberos, y lo pague con impuestos a la propiedad durante muchos años.</p>
  <ul>
    <li><strong>La mayoría de los bonos necesitan dos tercios de votos a favor.</strong> Esto viene de la Constitución de Idaho. Un bono escolar puede recibir el 60 por ciento y aun así no aprobarse.</li>
    <li><strong>Unos pocos solo necesitan mayoría simple,</strong> como los bonos para sistemas de agua y de drenaje.</li>
  </ul>

  <h2>Impuestos (levies): impuestos a la propiedad por un tiempo fijo</h2>
  <ul>
    <li><strong>Los impuestos suplementarios ("supplemental levies")</strong> pagan la operación de las escuelas, como el personal, los programas y los autobuses, por lo general por uno o dos años. Se aprueban con mayoría simple.</li>
    <li><strong>Los impuestos para instalaciones escolares ("plant facilities levies")</strong> pagan edificios escolares y reparaciones durante varios años sin pedir prestado. Necesitan por lo menos el 55 por ciento, y más si el impuesto es más grande.</li>
    <li><strong>Otros distritos,</strong> como los de bomberos y de bibliotecas, también pueden pedirles a los votantes que suban sus impuestos. El porcentaje de votos a favor que se necesita depende del tipo de impuesto y de cuánto tiempo dura, así que revise el texto de la boleta.</li>
  </ul>

  <h2>Cuándo aparecen en la boleta</h2>
  <ul>
    <li><strong>Las medidas escolares</strong> solo pueden aparecer en mayo o en noviembre. La Legislatura eliminó las fechas de elección de marzo y agosto.</li>
    <li><strong>Los bonos y los impuestos (levies) de la ciudad y del condado</strong> van el tercer martes de mayo o el día de la elección de noviembre.</li>
    <li><strong>Las iniciativas y los referendos de la ciudad</strong> se votan solo en la elección de noviembre de los años impares (Código de Idaho § 34-1801B).</li>
  </ul>

  <h2>Iniciativas y referendos locales</h2>
  <p>Los votantes de las ciudades y los condados de Idaho pueden proponer una ordenanza, u obligar a que se vote sobre una que el concejo o los comisionados acaban de aprobar.</p>
  <ul>
    <li><strong>Firmas:</strong> el 20 por ciento del número de personas que votaron en la última elección general de la ciudad (para una ciudad) o en la última elección general del condado (para un condado).</li>
    <li><strong>Plazo para un referendo:</strong> para una ciudad, dentro de los 60 días después de que se publica la ordenanza (Código de Idaho § 34-1801B). Pregunte al secretario (clerk) del condado cuál es el plazo para un condado.</li>
    <li><strong>Límites:</strong> las iniciativas locales no se pueden usar para decisiones de zonificación.</li>
    <li><strong>Para aprobarse:</strong> mayoría simple.</li>
  </ul>

  <h2>Antes de votar</h2>
  <ul>
    <li><strong>Lea el texto de la boleta.</strong> Debe indicar el propósito, la cantidad y el costo estimado por cada $100,000 de valor gravable.</li>
    <li><strong>Revise si reemplaza algo.</strong> Un impuesto que "renueva" uno que está por vencer quizás no suba lo que usted paga. Uno nuevo sí lo subirá.</li>
    <li><strong>Busque su boleta de muestra</strong> con el secretario (clerk) de su condado o en VoteIdaho.gov.</li>
    <li><strong>Vaya a la audiencia.</strong> La junta tiene que votar en una reunión pública para poner una medida en la boleta, mucho antes de la elección.</li>
    <li><strong>Revise quién puede votar y firmar.</strong> Para votar o firmar una petición en Idaho, debe ser ciudadano de EE. UU., tener por lo menos 18 años, haber vivido en Idaho y en su condado por lo menos 30 días y estar registrado para votar (Código de Idaho § 34-402). Los residentes permanentes (green card) y otras personas que no son ciudadanas no pueden votar ni firmar peticiones, ni siquiera en elecciones locales.</li>
  </ul>
""",
    sources=[("https://legislature.idaho.gov/statutesrules/idstat/Title34/T34CH18/SECT34-1801B/", "Código de Idaho § 34-1801B, iniciativas y referendos de las ciudades, Legislatura de Idaho (en inglés)"),
             ("https://legislature.idaho.gov/statutesrules/idstat/title34/t34ch4/sect34-402", "Código de Idaho § 34-402, quién puede votar, Legislatura de Idaho (en inglés)"),
             ("https://ballotpedia.org/Laws_governing_local_ballot_measures_in_Idaho", "Leyes sobre las medidas locales en la boleta en Idaho, Ballotpedia (en inglés)"),
             ("https://ballotpedia.org/School_bond_and_tax_elections_in_Idaho", "Elecciones de bonos e impuestos escolares en Idaho, Ballotpedia (en inglés)"),
             ("https://www.idahoednews.org/top-news/emerging-outliers-school-facility-measures-grow-harder-to-pass/", "Medidas para instalaciones escolares y el porcentaje que necesitan para aprobarse, Idaho Education News, junio de 2026 (en inglés)"),
             ("https://voteidaho.gov/county-clerk/", "Oficinas electorales de los condados, Secretaría de Estado de Idaho (en inglés)")])

G["two-minute-pitch"] = dict(
    cat="Habilidades", title="Prepare una presentación de dos minutos para su causa",
    lede="Un comentario público, una conversación en el pasillo con un legislador, una reunión con un comisionado: casi todas las oportunidades de defender su causa duran unos dos minutos. Así se aprovechan.",
    body="""
  <h2>La forma de una buena presentación</h2>
  <ol>
    <li><strong>Quién es usted (10 segundos).</strong> Su nombre, dónde vive y por qué le importa el tema: "Tengo hijos y vivo en Nampa", "Tengo un pequeño negocio en Sandpoint".</li>
    <li><strong>El problema (30 segundos).</strong> Una frase clara sobre lo que está mal, y luego un ejemplo breve y concreto. Una historia real vale más que una estadística, y una historia con un solo número vale más que las dos.</li>
    <li><strong>La solución (30 segundos).</strong> Lo que quiere que se haga, lo más concreto posible: un número de proyecto de ley, una línea del presupuesto, un punto de la agenda, un cambio a una política.</li>
    <li><strong>Por qué vale la pena (30 segundos).</strong> A quién beneficia, cuánto cuesta o cuánto ahorra, y quién más lo apoya.</li>
    <li><strong>La petición (10 segundos).</strong> Diga exactamente qué quiere que haga esa persona: votar a favor, copatrocinar el proyecto, reunirse con usted, ponerlo en una agenda.</li>
  </ol>

  <h2>Cómo lograr que convenza</h2>
  <ul>
    <li><strong>Conozca a su público.</strong> ¿Qué le importa a esa persona? ¿Qué ha dicho o cómo ha votado antes? Relacione su tema con eso.</li>
    <li><strong>Una petición, no cinco.</strong> Escoja la cosa que más importa en este momento.</li>
    <li><strong>Practique en voz alta y mida el tiempo.</strong> Dos minutos son unas 250 palabras habladas. Los presidentes de los comités legislativos muchas veces limitan los testimonios a dos o tres minutos y le van a cortar.</li>
    <li><strong>Deje algo por escrito.</strong> Un resumen de una página con sus datos de contacto.</li>
    <li><strong>Haga seguimiento.</strong> Mande un agradecimiento dentro de un día y repita su petición.</li>
  </ul>

  <h2>Cómo contar su propia historia</h2>
  <p>Si habla de su experiencia personal, comparta solo lo que se sienta cómodo dejando en el registro público. Las reuniones muchas veces se graban y se publican en internet, y las audiencias de los comités de la Legislatura se transmiten en vivo.</p>
""",
    sources=[("https://legislature.idaho.gov/resources/committeetestimony/", "Cómo testificar ante comités legislativos, Legislatura de Idaho (en inglés)")])

G["read-a-bill-or-agenda"] = dict(
    cat="Habilidades", title="Cómo leer un proyecto de ley o una agenda",
    lede="Los proyectos de ley y las agendas parecen complicados, pero siguen patrones. Cuando conoce los patrones, puede encontrar lo importante en unos minutos.",
    body="""
  <h2>Cómo leer el número de un proyecto de ley de Idaho</h2>
  <ul>
    <li><strong>H 123</strong> es un proyecto de ley de la Cámara de Representantes (House). <strong>S 1045</strong> es un proyecto de ley del Senado. Los proyectos del Senado empiezan en el 1001, así que un número de cuatro cifras quiere decir que empezó en el Senado.</li>
    <li><strong>Una "a" minúscula quiere decir que fue enmendado.</strong> H 123a ha sido enmendado una vez y H 123aa dos veces. "aaS" quiere decir que una de esas enmiendas se hizo en el Senado.</li>
    <li><strong>HJR y SJR</strong> son resoluciones conjuntas, que se usan para proponer enmiendas a la Constitución de Idaho. Estas van a votación del pueblo.</li>
    <li><strong>HCR y SCR</strong> son resoluciones concurrentes, que se usan para los asuntos internos de la Legislatura y para aprobar o rechazar los reglamentos de las agencias.</li>
    <li><strong>HJM y SJM</strong> son memoriales conjuntos: mensajes formales al Congreso o al Presidente. No cambian la ley de Idaho.</li>
    <li><strong>RS</strong> seguido de un número es un borrador que todavía no se ha presentado. Se convierte en proyecto de ley cuando un comité vota para imprimirlo.</li>
  </ul>

  <h2>Cómo leer el proyecto de ley</h2>
  <ol>
    <li><strong>Empiece con la declaración de propósito ("Statement of Purpose").</strong> Cada proyecto de ley de Idaho viene con una página que explica lo que hace y una estimación del impacto fiscal ("fiscal note") que calcula cuánto cuesta. Las dos las escribe quien patrocina el proyecto, así que léalas como los argumentos de esa persona, no como un análisis neutral.</li>
    <li><strong>Lea el título.</strong> La oración larga de arriba nombra cada sección de la ley que toca el proyecto.</li>
    <li><strong>Busque las marcas.</strong> El texto <u>subrayado</u> se agrega a la ley. El texto <s>tachado</s> se quita. El texto normal es la ley actual que se queda igual.</li>
    <li><strong>Revise la última sección.</strong> Dice cuándo entra en vigor la ley. La mayoría entra en vigor el 1 de julio. Una "cláusula de emergencia" ("emergency clause") hace que entre en vigor en cuanto el Gobernador la firma.</li>
    <li><strong>Revise la página del proyecto</strong> en el sitio web de la Legislatura para ver su historial: dónde está ahora y cómo votó cada miembro. Los proyectos de ley y esa página están en inglés.</li>
  </ol>

  <h2>Cómo leer una agenda local</h2>
  <ul>
    <li><strong>Puntos de acción ("action items").</strong> La ley de Idaho exige que todo lo que la junta va a votar se marque como punto de acción. Si su tema no está marcado así, no se va a decidir en esa reunión.</li>
    <li><strong>Agenda de consentimiento ("consent agenda").</strong> Asuntos de rutina que se aprueban en una sola votación, sin discusión. Un miembro de la junta puede sacar un asunto para discutirlo, y usted puede pedirle a uno que lo haga.</li>
    <li><strong>Audiencias públicas.</strong> Asuntos en los que la ley exige que la junta escuche testimonios. Cada una indica qué se va a decidir.</li>
    <li><strong>Sesión a puerta cerrada ("executive session").</strong> Una parte privada de la reunión. La agenda debe citar la sección del Código de Idaho que la permite, y ahí no se puede tomar ninguna decisión final.</li>
    <li><strong>El paquete de documentos ("packet").</strong> Los informes del personal, los mapas y los borradores de ordenanzas que respaldan cada asunto. Por lo general es un archivo aparte, mucho más largo, y es donde están los detalles.</li>
  </ul>

  <h2>Atajos</h2>
  <ul>
    <li><strong>Busque en el archivo</strong> el nombre de su calle, de su escuela o la palabra clave.</li>
    <li><strong>Lea primero la recomendación del personal.</strong> Las juntas la siguen la mayoría de las veces.</li>
    <li><strong>Pregúntele al secretario (clerk) o al secretario del comité</strong> cuando algo no esté claro. Contestar ese tipo de preguntas es parte de su trabajo.</li>
  </ul>
""",
    sources=[("https://legislature.idaho.gov/resources/howabillbecomesalaw/", "Cómo un proyecto de ley se convierte en ley, Legislatura de Idaho (en inglés)"),
             ("https://legislature.idaho.gov/", "Texto de los proyectos de ley, declaraciones de propósito e historial, Legislatura de Idaho (en inglés)"),
             ("https://legislature.idaho.gov/statutesrules/idstat/Title74/T74CH2/", "Código de Idaho, Título 74, Capítulo 2: Ley de Reuniones Abiertas, Legislatura de Idaho (en inglés)")])

G["media-literacy"] = dict(
    cat="Habilidades", title="Alfabetización mediática: cómo distinguir la buena información de la mala",
    lede="Antes de compartir algo, discutirlo o ir a una reunión, vale la pena saber si lo que leyó es cierto. Estos hábitos toman un minuto y detectan la mayoría de los problemas.",
    body="""
  <h2>Antes de creerlo</h2>
  <ul>
    <li><strong>Revise la fuente.</strong> ¿Quién lo publicó? ¿Tiene buena trayectoria y corrige sus errores? Un sitio desconocido que parece un medio de noticias puede no serlo.</li>
    <li><strong>Lea más allá del titular.</strong> Los titulares se escriben para atraer clics y muchas veces exageran lo que dice la nota.</li>
    <li><strong>Busque el original.</strong> Si una publicación cita un estudio, una ley o una frase, busque el original. Los proyectos de ley, las agendas, los presupuestos y los expedientes de las cortes por lo general son públicos.</li>
    <li><strong>Revise la fecha.</strong> Las noticias viejas se vuelven a compartir como si fueran nuevas.</li>
    <li><strong>Vea quién más lo está reportando.</strong> Si una afirmación grande aparece en un solo lugar, espere.</li>
  </ul>

  <h2>Tenga cuidado con esto</h2>
  <ul>
    <li><strong>Las emociones fuertes.</strong> El contenido hecho para enojarle o asustarle es el que más rápido se difunde. Esa es una señal para ir más despacio.</li>
    <li><strong>Imágenes y videos editados o falsos,</strong> incluidos los hechos con inteligencia artificial. Fíjese en detalles raros y busque la imagen para ver dónde apareció primero.</li>
    <li><strong>Falta de contexto.</strong> Un video o un número real puede engañar cuando está recortado.</li>
    <li><strong>Resúmenes de proyectos de ley hechos por grupos de presión.</strong> Grupos de todos los lados califican y resumen los proyectos de ley de Idaho. Lea el texto del proyecto antes de confiar en lo que cualquiera diga de él.</li>
  </ul>

  <h2>Las noticias locales importan</h2>
  <p>Los reporteros locales cubren los concejos municipales, las juntas escolares y las decisiones del condado que los medios nacionales nunca van a cubrir. Muchos pueblos de Idaho se han quedado sin su periódico diario. Apoyar las noticias locales que todavía tiene, y leerlas, es una de las maneras más fáciles de estar al tanto de las decisiones que se toman cerca de usted.</p>

  <h2>Vaya a la fuente cuando se trata del gobierno</h2>
  <p>Para las decisiones locales y estatales, las fuentes originales casi siempre están en internet: las agendas y grabaciones de las reuniones, las páginas de los proyectos de ley de la Legislatura y su video en vivo, y los informes de las agencias. El <a href="../">calendario</a> tiene un enlace a la página oficial de cada reunión. Para las elecciones, el secretario (clerk) de su condado y VoteIdaho.gov son la palabra oficial sobre fechas, lugares de votación y resultados.</p>
""",
    sources=[("https://www.newslit.org/", "News Literacy Project, organización de alfabetización en noticias (en inglés)"),
             ("https://voteidaho.gov/", "VoteIdaho.gov, Secretaría de Estado de Idaho (en inglés)"),
             ("https://www.idahoptv.org/shows/idahoinsession/Legislature/", "Idaho in Session, video en vivo de la Legislatura, Idaho Public Television (en inglés)")])

G["volunteer-and-public-service"] = dict(
    cat="Vida diaria", title="Voluntariado y trabajos en el servicio público",
    lede="Ir a las reuniones es una manera de participar. Dar su tiempo, o hacer del servicio público su trabajo, es otra.",
    body="""
  <h2>Sea voluntario</h2>
  <ul>
    <li><strong>Serve Idaho</strong> es la comisión del Gobernador para el servicio y el voluntariado. Maneja los programas de AmeriCorps en Idaho y orienta a la gente hacia oportunidades de voluntariado en todo el estado.</li>
    <li><strong>Trabaje en los centros de votación.</strong> Los secretarios (clerks) de los condados contratan trabajadores electorales para cada elección. Es un trabajo pagado, toma un día largo y a los secretarios casi siempre les falta gente. Los trabajadores electorales deben ser ciudadanos de EE. UU., tener por lo menos 16 años y saber leer y escribir en inglés, según la Secretaría de Estado de Idaho. Comuníquese con la oficina electoral de su condado.</li>
    <li><strong>Su biblioteca, su escuela y sus parques.</strong> La mayoría acepta voluntarios directamente. Los grupos de Amigos de la Biblioteca (Friends of the Library) y las organizaciones de padres de familia son lugares fáciles para empezar.</li>
    <li><strong>Búsqueda y rescate, bomberos y ambulancias.</strong> Gran parte del Idaho rural depende de personal de emergencia voluntario, que por lo general se organiza por medio de la oficina del alguacil (sheriff) o del distrito de bomberos local.</li>
    <li><strong>Los parques estatales y Fish and Game</strong> (el departamento de pesca y caza de Idaho) tienen programas de voluntariado, desde anfitriones de campamentos hasta proyectos para proteger el hábitat de la fauna.</li>
  </ul>

  <h2>Sirva en una junta</h2>
  <p>Las comisiones de planeación, las juntas de bibliotecas y los consejos asesores del estado se llenan con residentes. Vea <a href="boards-and-commissions.html">cómo servir en una junta o comisión</a>.</p>

  <h2>Trabaje en el gobierno</h2>
  <ul>
    <li><strong>Trabajos del estado.</strong> La Idaho Division of Human Resources (la división de recursos humanos del estado) publica las vacantes de las agencias estatales y explica cómo funciona la contratación.</li>
    <li><strong>Los trabajos de la ciudad, del condado y del distrito escolar</strong> se publican en el sitio web de cada gobierno.</li>
    <li><strong>IdahoWorks,</strong> del Idaho Department of Labor (el departamento del trabajo de Idaho), publica trabajos públicos y privados en todo el estado.</li>
    <li><strong>Los trabajos federales</strong> en Idaho, incluidos los del Forest Service (servicio forestal), el Bureau of Land Management (la oficina de administración de tierras federales) y las oficinas federales del Idaho National Laboratory, se publican en USAJOBS.</li>
    <li><strong>La Legislatura</strong> contrata personal para la sesión legislativa cada invierno, incluidos secretarios de comité y pajes (pages). Los estudiantes del último año de preparatoria pueden solicitar ser pajes.</li>
  </ul>

  <h2>Postúlese a un cargo</h2>
  <p>En muchos puestos locales se presenta un solo candidato. Vea <a href="running-for-office.html">cómo postularse a un cargo</a>.</p>
""",
    sources=[("https://serve.idaho.gov/", "Serve Idaho, la comisión del Gobernador para el servicio y el voluntariado (en inglés)"),
             ("https://dhr.idaho.gov/information-about-state-careers/", "Información sobre empleos en el estado, Idaho Division of Human Resources (en inglés)"),
             ("https://idahoworks.gov/", "IdahoWorks, Idaho Department of Labor (en inglés)"),
             ("https://voteidaho.gov/poll-workers/", "Cómo ser trabajador electoral, Secretaría de Estado de Idaho (en inglés)"),
             ("https://voteidaho.gov/county-clerk/", "Oficinas electorales de los condados, Secretaría de Estado de Idaho (en inglés)"),
             ("https://www.usajobs.gov/", "USAJOBS, empleos del gobierno federal (en inglés)")])

G["problem-to-policy"] = dict(
    cat="Resolver problemas", title="Cómo convertir un problema personal en una propuesta de política pública",
    lede="Muchas leyes empezaron con la mala experiencia de una sola persona. Así puede saber si su problema tiene una solución del gobierno, y cómo pedirla.",
    body="""
  <h2>¿Es un problema personal o del gobierno?</h2>
  <p>Hágase tres preguntas:</p>
  <ul>
    <li><strong>¿Les pasa también a otras personas?</strong> Si sus vecinos, sus compañeros de trabajo o personas en internet cuentan lo mismo, puede ser un patrón y no mala suerte.</li>
    <li><strong>¿Lo causa una regla, o una regla no lo evita?</strong> Una cuota, un plazo, un servicio que falta, una ley que no corresponde a cómo vive la gente.</li>
    <li><strong>¿Hay un órgano de gobierno responsable de esa regla?</strong> Si es así, tiene a quién pedirle.</li>
  </ul>

  <h2>Encuentre el nivel correcto</h2>
  <ul>
    <li><strong>Empiece con la agencia que maneja el programa.</strong> Muchos problemas tienen que ver con cómo se aplica una regla, no con la regla misma, y la agencia puede arreglarlos.</li>
    <li><strong>Si el problema es la regla misma,</strong> averigüe quién la hizo: un concejo municipal, los comisionados del condado, la junta de un distrito, la Legislatura, los reglamentos de una agencia estatal o el Congreso. Vea <a href="contact-your-representatives.html">cómo comunicarse con quienes le representan</a>.</li>
    <li><strong>Los reglamentos de las agencias tienen una segunda revisión.</strong> En Idaho, los reglamentos de las agencias estatales tienen que pasar por la Legislatura, que puede rechazarlos. Si su problema es un reglamento, el período de comentarios de la agencia sobre ese reglamento y el comité legislativo que lo revisa son dos lugares para hacerse escuchar.</li>
  </ul>

  <h2>Dé forma a su petición</h2>
  <ol>
    <li><strong>Describa el problema en una frase.</strong></li>
    <li><strong>Muestre que no le pasa solo a usted.</strong> Reúna algunas historias más, y los números que pueda encontrar.</li>
    <li><strong>Proponga un cambio concreto.</strong> "Que la gente pueda renovar en línea", "ampliar el plazo a 30 días", "agregar una exención para quienes no pueden pagar". No necesita lenguaje legal perfecto.</li>
    <li><strong>Busque aliados.</strong> Organizaciones sin fines de lucro, grupos de negocios, iglesias o asociaciones de vecinos quizás ya estén trabajando en el tema.</li>
    <li><strong>Busque a alguien que lo defienda.</strong> Un funcionario electo que de verdad lleve la idea adelante vale más que diez que están de acuerdo de pasada. En la Legislatura, un proyecto de ley necesita un patrocinador y un presidente de comité dispuesto a darle una audiencia.</li>
  </ol>

  <h2>Tenga en cuenta el calendario</h2>
  <p>La Legislatura de Idaho se reúne unos tres meses a partir de enero, y los proyectos de ley que no se aprueban mueren cuando termina la sesión legislativa. El momento de llevarle una idea a un legislador es el verano y el otoño, cuando está en casa y preparando proyectos. Para febrero, por lo general ya es demasiado tarde para ese año.</p>

  <h2>Prepárese para un camino largo</h2>
  <p>La mayoría de los cambios toman más de un intento. Muchas veces un proyecto de ley tarda varias sesiones legislativas en aprobarse, y los cambios locales pueden tener que esperar al siguiente presupuesto. Lleve un registro de cada conversación, mantenga informados a sus aliados y vuelva a intentarlo.</p>
  <p>Cuando esté listo para defender su causa en persona, use <a href="two-minute-pitch.html">cómo preparar una presentación de dos minutos</a>.</p>
""",
    sources=[("https://legislature.idaho.gov/resources/howabillbecomesalaw/", "Cómo un proyecto de ley se convierte en ley, Legislatura de Idaho (en inglés)"),
             ("https://legislature.idaho.gov/resources/committeetestimony/", "Cómo testificar ante comités legislativos, Legislatura de Idaho (en inglés)")])

G["legislature"] = dict(
    cat="Estado", title="Cómo funciona la Legislatura de Idaho",
    lede="Ciento cinco legisladores de medio tiempo escriben las leyes y el presupuesto de Idaho en unos tres meses cada invierno. Esto es quiénes son, cómo funciona la sesión legislativa y dónde cuenta su voz.",
    body="""
  <h2>Quiénes la forman</h2>
  <ul>
    <li><strong>35 distritos.</strong> Cada uno elige a un senador y a dos representantes, en los escaños A y B de la Cámara de Representantes. En total son 35 senadores y 70 representantes. Sus tres legisladores representan al mismo distrito.</li>
    <li><strong>Periodos de dos años para todos.</strong> Todos los escaños de ambas cámaras están en la boleta cada año par. No hay límite de periodos.</li>
    <li><strong>Los nuevos periodos empiezan el 1 de diciembre</strong> después de la elección de noviembre. Los miembros se reúnen brevemente a principios de diciembre para organizarse y elegir a sus líderes.</li>
    <li><strong>Es un trabajo de medio tiempo.</strong> La mayoría de los legisladores tiene otro trabajo y está en su distrito desde la primavera hasta diciembre.</li>
    <li><strong>Los límites de los distritos</strong> se vuelven a trazar después de cada censo. Lo hace una comisión de ciudadanos de ambos partidos, no la Legislatura.</li>
  </ul>
  <p>Encuentre a los suyos en <a href="../reps.html">Quién le representa</a>.</p>

  <h2>El calendario de la sesión</h2>
  <ul>
    <li><strong>Empieza a principios de enero.</strong> La sesión legislativa abre el lunes más cercano al 9 de enero. En 2027 es el 11 de enero. Ese día el Gobernador da el discurso sobre el Estado del Estado ("State of the State") y presenta su propuesta de presupuesto.</li>
    <li><strong>No tiene fecha fija de cierre.</strong> La sesión dura hasta que se termina el trabajo, normalmente unos tres meses, y acaba a finales de marzo o en abril.</li>
    <li><strong>Todo muere al final.</strong> Un proyecto de ley que no se aprobó cuando la Legislatura cierra la sesión queda muerto. Hay que volver a presentarlo el año siguiente.</li>
    <li><strong>Entre sesiones,</strong> los comités interinos estudian temas específicos y el comité de presupuesto se reúne algunas veces. Esas reuniones están en el <a href="../?cat=legislature">calendario</a>.</li>
  </ul>

  <h2>Cómo avanza un proyecto de ley</h2>
  <ol class="steps">
    <li><strong>Un borrador, llamado RS.</strong> Un legislador pide que se redacte una idea. Antes de que sea proyecto de ley, un comité hace una audiencia corta para imprimirlo ("print hearing") y vota si lo presenta. En este paso no se recibe testimonio del público.</li>
    <li><strong>Presentación.</strong> El proyecto recibe un número, se lee en el pleno y se envía a un comité.</li>
    <li><strong>Audiencia del comité.</strong> El presidente del comité decide si el proyecto tiene audiencia y cuándo. Aquí es donde el público da su testimonio. El comité puede mandar el proyecto al pleno con la recomendación de aprobarlo ("do pass"), mandarlo a enmiendas o retenerlo, lo que normalmente lo mata.</li>
    <li><strong>Votación en el pleno.</strong> El proyecto se lee en tres días distintos. El debate y la votación ocurren en la tercera lectura. Se aprueba con la mayoría de los miembros presentes.</li>
    <li><strong>La otra cámara.</strong> Ahí pasa por los mismos pasos. Si la segunda cámara lo enmienda, la primera tiene que estar de acuerdo.</li>
    <li><strong>El Gobernador.</strong> Durante la sesión, el Gobernador tiene cinco días, sin contar los domingos, para firmarlo o vetarlo. Si no hace nada, el proyecto se vuelve ley sin su firma. Después de que la Legislatura cierra la sesión, el Gobernador tiene diez días. Un veto se puede anular con dos tercios de los miembros presentes en cada cámara.</li>
    <li><strong>Entra en vigor.</strong> La mayoría de las leyes nuevas entran en vigor el 1 de julio.</li>
  </ol>

  <h2>Fechas límite dentro de la sesión</h2>
  <ul>
    <li><strong>Cada miembro puede presentar proyectos por su cuenta solo en las primeras semanas:</strong> hasta el día 12 en el Senado y el día 20 en la Cámara de Representantes. Después, los proyectos tienen que venir de un comité, y después del día 36 en la Cámara solo de ciertos comités.</li>
    <li><strong>Los líderes fijan fechas meta</strong> cada año para pasar proyectos de una cámara a la otra. Muchas veces se atrasan.</li>
    <li><strong>El final de la sesión va muy rápido.</strong> En las últimas semanas, los proyectos pueden recibir audiencia y aprobarse con muy poco aviso.</li>
  </ul>

  <h2>El comité de presupuesto</h2>
  <p>El Comité Conjunto de Finanzas y Asignaciones (Joint Finance-Appropriations Committee), conocido como JFAC, son diez senadores y diez representantes que escriben el presupuesto de cada agencia. Es el comité con más poder en el Capitolio. Vea <a href="state-budgets.html">el presupuesto estatal y cómo influir en él</a>.</p>

  <h2>Dónde cuenta su voz</h2>
  <ul>
    <li><strong>Antes de la sesión.</strong> En el verano y el otoño los legisladores deciden qué proyectos van a patrocinar. Están en casa y es fácil comunicarse con ellos.</li>
    <li><strong>El presidente del comité.</strong> Un proyecto que nunca tiene audiencia nunca llega a votación. Si usted quiere que un proyecto reciba audiencia, o que no la reciba, el presidente es quien decide.</li>
    <li><strong>La audiencia del comité.</strong> Es el único paso con testimonio del público. Vea <a href="weigh-in-on-a-state-bill.html">cómo opinar sobre un proyecto de ley estatal</a>.</li>
    <li><strong>Sus tres legisladores,</strong> antes de la votación en el pleno.</li>
    <li><strong>La oficina del Gobernador,</strong> una vez que el proyecto pasó por ambas cámaras.</li>
  </ul>
""",
    sources=[("https://legislature.idaho.gov/resources/howabillbecomesalaw/", "Cómo un proyecto se convierte en ley, Legislatura de Idaho (en inglés)"),
             ("https://legislature.idaho.gov/legislators/", "Legisladores, Legislatura de Idaho (en inglés)"),
             ("https://legislature.idaho.gov/committees/", "Comités, Legislatura de Idaho (en inglés)"),
             ("https://legislature.idaho.gov/statutesrules/idconst/", "Constitución de Idaho, Artículos III y IV, Legislatura de Idaho (en inglés)"),
             ("https://www.idahoptv.org/shows/idahoinsession/Legislature/", "Idaho in Session, video en vivo de la Legislatura, Idaho Public Television (en inglés)")])

G["weigh-in-on-a-state-bill"] = dict(
    cat="Estado", title="Cómo opinar sobre un proyecto de ley estatal",
    lede="La sesión legislativa de Idaho es corta y las audiencias se programan rápido. Estas son cuatro maneras de decirle a la Legislatura lo que usted piensa, y los tiempos que sorprenden a mucha gente.",
    body="""
  <h2>1. Comuníquese con sus propios legisladores</h2>
  <p>Usted tiene un senador y dos representantes. Un correo corto que nombre el proyecto de ley y diga que usted vive en el distrito es lo más sencillo que puede hacer, y funciona en cualquier etapa. Encuéntrelos en <a href="../reps.html">Quién le representa</a>. Durante la sesión también puede llamar al Centro de Información Legislativa (Legislative Information Center) al 208-332-1000 o al 800-626-0471.</p>

  <h2>2. Dé su testimonio en la audiencia del comité</h2>
  <p>La audiencia del comité es el único momento en que habla el público.</p>
  <ol>
    <li><strong>Encuentre la audiencia.</strong> Cada comité publica una agenda con los proyectos que va a tratar en audiencia. Las agendas están en el sitio web de la Legislatura y en el <a href="../?cat=legislature">calendario</a>.</li>
    <li><strong>Inscríbase.</strong> La agenda y la página web del comité tienen un enlace a un formulario de inscripción para dar testimonio (en inglés). Le pedirán su nombre, su dirección, el grupo que representa si es el caso, si está a favor o en contra, y si estará en persona o a distancia.</li>
    <li><strong>El testimonio a distancia depende del comité.</strong> La mayoría de los presidentes de comité permiten testimonio por video o por teléfono, pero no todos, y no en todas las reuniones. El formulario de inscripción indica si se ofrece.</li>
    <li><strong>Cuente con dos o tres minutos.</strong> El presidente pone el límite de tiempo y puede limitar el total de testimonios. Inscribirse no garantiza que le llamen.</li>
    <li><strong>Siga las reglas de la sala.</strong> No se permiten aplausos, letreros ni manifestaciones. El presidente puede pedir a la gente que salga.</li>
  </ol>

  <h2>3. Envíe su testimonio por escrito</h2>
  <p>Mande su testimonio escrito por correo electrónico al secretario del comité. Su dirección está en la página del comité. La Legislatura recomienda enviarlo aunque piense hablar, por si se acaba el tiempo o falla la conexión a distancia. Que no pase de una página, y ponga el número del proyecto y su posición en la primera línea.</p>

  <h2>4. Escriba al presidente del comité y al Gobernador</h2>
  <ul>
    <li><strong>El presidente</strong> decide si un proyecto tiene audiencia o no. Si un proyecto que le importa está detenido en el comité, el presidente es la persona a quien debe preguntar.</li>
    <li><strong>El Gobernador</strong> tiene cinco días, sin contar los domingos, para firmar o vetar un proyecto que le llega durante la sesión. La oficina del Gobernador recibe mensajes por teléfono y por un formulario en su sitio web.</li>
  </ul>

  <h2>Los tiempos que sorprenden</h2>
  <ul>
    <li><strong>Las audiencias se pueden programar con muy poco aviso,</strong> a veces de un día. Revise la agenda todos los días cuando un proyecto que le importa esté en el comité.</li>
    <li><strong>Las agendas cambian.</strong> Los proyectos se retiran o se mueven, y una audiencia puede no ocurrir en la fecha en que se anunció primero.</li>
    <li><strong>La primera audiencia no es una audiencia.</strong> Cuando se presenta un borrador por primera vez, el comité solo vota si lo imprime. El testimonio viene después, en la audiencia completa.</li>
    <li><strong>Tiene dos oportunidades.</strong> Un proyecto que pasa una cámara tiene una nueva audiencia de comité en la otra.</li>
    <li><strong>Nada pasa al año siguiente.</strong> Un proyecto que no se aprueba antes del final de la sesión queda muerto y tiene que empezar de nuevo el siguiente enero.</li>
  </ul>

  <h2>Véalo desde cualquier lugar</h2>
  <p>Idaho Public Television transmite en vivo las sesiones del pleno y las audiencias de los comités por medio de Idaho in Session, y el sitio web de la Legislatura guarda los videos. La página de cada proyecto muestra su texto, su declaración de propósito ("statement of purpose"), en qué etapa está y cómo votaron los miembros. Todo está en inglés.</p>
""",
    sources=[("https://legislature.idaho.gov/resources/committeetestimony/", "Cómo testificar ante comités legislativos, Legislatura de Idaho (en inglés)"),
             ("https://legislature.idaho.gov/remote-testimony/", "Testimonio a distancia, Legislatura de Idaho (en inglés)"),
             ("https://legislature.idaho.gov/committees/senatecommittees/", "Comités del Senado, con los contactos de sus secretarios, Legislatura de Idaho (en inglés)"),
             ("https://legislature.idaho.gov/committees/housecommittees/", "Comités de la Cámara de Representantes, con los contactos de sus secretarios, Legislatura de Idaho (en inglés)"),
             ("https://www.idahoptv.org/shows/idahoinsession/Legislature/", "Idaho in Session, Idaho Public Television (en inglés)")])

G["state-budgets"] = dict(
    cat="Estado", title="El presupuesto estatal y cómo influir en él",
    lede="Idaho no aprueba un solo gran proyecto de presupuesto. Aprueba un proyecto de gastos aparte para cada agencia, y todos los escribe un solo comité. Este es el ciclo de cada año y cuándo puede participar usted en cada parte.",
    body="""
  <h2>Lo básico</h2>
  <ul>
    <li><strong>El año fiscal</strong> va del 1 de julio al 30 de junio. El año fiscal 2028 empieza el 1 de julio de 2027.</li>
    <li><strong>Tiene que estar equilibrado.</strong> La Constitución de Idaho no permite que el estado gaste más de lo que espera recibir.</li>
    <li><strong>Tres tipos de dinero.</strong> El Fondo General (General Fund) viene sobre todo de los impuestos sobre la renta y sobre las ventas, y es lo que discuten los legisladores. Los fondos dedicados son cuotas e impuestos atados a un propósito, como los impuestos a la gasolina para las carreteras. Los fondos federales vienen con reglas federales.</li>
    <li><strong>Las escuelas públicas son la parte más grande</strong> del Fondo General, seguidas por salud y servicios humanos.</li>
  </ul>

  <h2>El ciclo de cada año</h2>
  <ol class="steps">
    <li><strong>Verano: las agencias preparan sus solicitudes.</strong> A partir de julio, cada agencia escribe su solicitud para el siguiente año fiscal, siguiendo las instrucciones de la oficina de presupuesto del Gobernador.</li>
    <li><strong>1 de septiembre: se entregan las solicitudes.</strong> Las agencias las envían a la División de Administración Financiera del Gobernador (Division of Financial Management) y al personal de presupuesto de la Legislatura. Las solicitudes son públicas.</li>
    <li><strong>Otoño: el Gobernador decide.</strong> El personal del Gobernador revisa las solicitudes y el Gobernador define su recomendación.</li>
    <li><strong>Enero: el presupuesto del Gobernador.</strong> Se publica el primer día de la sesión legislativa. El Libro de Presupuesto Legislativo (Legislative Budget Book) pone lado a lado la solicitud de cada agencia y la recomendación del Gobernador.</li>
    <li><strong>Enero y febrero: JFAC.</strong> El Comité Conjunto de Finanzas y Asignaciones (Joint Finance-Appropriations Committee), diez senadores y diez representantes, escucha a cada agencia y luego vota cada presupuesto.</li>
    <li><strong>Febrero y marzo: los proyectos de ley.</strong> Cada decisión de JFAC se convierte en un proyecto de ley de asignación ("appropriation bill") que tiene que aprobarse en la Cámara de Representantes y en el Senado, y que debe firmar el Gobernador. Si uno no se aprueba, JFAC escribe uno nuevo.</li>
    <li><strong>1 de julio: entra en vigor.</strong></li>
  </ol>

  <h2>Dónde puede opinar</h2>
  <ul>
    <li><strong>Con la agencia, en la primavera y el verano.</strong> El momento más fácil para que algo entre en un presupuesto es antes de que se escriba la solicitud. Muchas agencias responden a una junta o comisión que aprueba la solicitud en una reunión pública.</li>
    <li><strong>Con la oficina del Gobernador, en el otoño.</strong></li>
    <li><strong>Con los miembros de JFAC, en diciembre y enero.</strong> Las audiencias de JFAC son sobre todo para que las agencias presenten, y el testimonio del público es poco común, así que el correo electrónico es la vía práctica. Empiece con los miembros de su región del estado.</li>
    <li><strong>Con sus propios legisladores, antes de las votaciones en el pleno.</strong> Cada proyecto de asignación se vota en ambas cámaras. Vea <a href="../reps.html">Quién le representa</a>.</li>
  </ul>

  <h2>Los presupuestos locales funcionan de otra manera</h2>
  <p>Su ciudad, su condado, su distrito escolar y otros distritos locales aprueban cada uno su propio presupuesto, y cada uno debe hacer antes una audiencia pública. Los condados y la mayoría de las ciudades empiezan su año fiscal el 1 de octubre y hacen la audiencia en agosto o a principios de septiembre. Los distritos escolares empiezan el 1 de julio y hacen la suya en junio. Esa audiencia está abierta a cualquier persona, y es donde se fijan los niveles locales del impuesto a la propiedad.</p>

  <h2>Siga el dinero</h2>
  <p>La oficina de presupuesto de la Legislatura publica el Libro de Presupuesto Legislativo antes de cada sesión y, después, un resumen sencillo de lo que se aprobó. El sitio web Transparent Idaho, del Contralor del Estado (State Controller), muestra los gastos del estado, la nómina y los presupuestos de los gobiernos locales. Estos documentos están en inglés.</p>
""",
    sources=[("https://dfm.idaho.gov/citizens/budget-process/", "El proceso del presupuesto, División de Administración Financiera de Idaho (en inglés)"),
             ("https://legislature.idaho.gov/lso/bpa/process/", "El proceso del presupuesto y las leyes que lo rigen, Oficina de Servicios Legislativos de Idaho (en inglés)"),
             ("https://legislature.idaho.gov/committees/joint-standing/", "Comités conjuntos permanentes, incluido el Comité Conjunto de Finanzas y Asignaciones (JFAC), Legislatura de Idaho (en inglés)"),
             ("https://legislature.idaho.gov/statutesrules/idconst/", "Constitución de Idaho, Artículo VII, Legislatura de Idaho (en inglés)")])

G["boards-and-commissions"] = dict(
    cat="Estado", title="Forme parte de una junta o comisión",
    lede="Cientos de decisiones en Idaho, desde la zonificación hasta las licencias profesionales y las temporadas de caza y pesca, las toman o las influyen juntas formadas por residentes comunes. La mayoría de los puestos se llenan por nombramiento, y muchos se quedan vacíos por falta de interesados.",
    body="""
  <h2>Qué hacen estas juntas</h2>
  <ul>
    <li><strong>Algunas deciden.</strong> Una comisión de planificación y zonificación resuelve sobre permisos. La Comisión de Pesca y Caza (Fish and Game Commission) fija las temporadas. Las juntas de licencias sancionan a profesionales.</li>
    <li><strong>Algunas aconsejan.</strong> Una junta de parques o un consejo asesor hace recomendaciones a los funcionarios electos que deciden.</li>
    <li><strong>La mayoría no pagan</strong> o pagan una cantidad pequeña por reunión, y se reúnen una o dos veces al mes.</li>
  </ul>

  <section class="near-you" data-show="boards" data-title="Juntas cerca de usted" aria-label="Juntas cerca de usted"></section>

  <h2>Juntas de la ciudad y del condado</h2>
  <ul>
    <li><strong>Ciudades:</strong> normalmente el alcalde nombra y el concejo municipal confirma. Las juntas comunes son planificación y zonificación, parques, la junta de la biblioteca, preservación histórica, artes y la agencia de renovación urbana.</li>
    <li><strong>Condados:</strong> los tres comisionados del condado nombran. Las juntas comunes son planificación y zonificación, la junta de la feria, el control de malezas y los puestos del condado en juntas regionales, como el distrito de salud pública.</li>
    <li><strong>Cómo solicitar:</strong> la mayoría tiene una solicitud corta en el sitio web de la ciudad o del condado, o con el secretario (clerk). Si no ve puestos vacantes anunciados, pregunte al secretario o a la oficina de los comisionados. Los condados pequeños muchas veces llenan los puestos de boca en boca, y basta con decir que le interesa para quedar en la lista.</li>
  </ul>

  <h2>Juntas, comisiones y consejos del estado</h2>
  <p>El Gobernador nombra a los miembros de las juntas estatales de Idaho. Muchos nombramientos también necesitan la confirmación del Senado.</p>
  <ol>
    <li><strong>Escoja una junta.</strong> La página de nombramientos del Gobernador (Appointments) tiene la lista completa de juntas, comisiones y consejos.</li>
    <li><strong>Revise las vacantes.</strong> Otra página muestra los puestos vacantes y los que se abrirán en los próximos 60 días. Muchos puestos tienen requisitos fijados por ley, como vivir en cierta región, pertenecer a cierto partido o tener cierta licencia.</li>
    <li><strong>Llene la solicitud.</strong> Es un formulario en la página de nombramientos, en inglés. Tiene que estar completo, firmado y con fecha, con su currículum adjunto.</li>
    <li><strong>Envíela por correo postal</strong> a la oficina del Gobernador, a la atención de Appointments. La dirección está en el formulario.</li>
    <li><strong>Una recomendación ayuda.</strong> Otra persona puede recomendarle por medio de un formulario en la misma página. Una nota de su legislador también ayuda.</li>
  </ol>
  <p>Si tiene preguntas, llame a la oficina del Gobernador al 208-334-2100.</p>

  <h2>Antes de solicitar</h2>
  <ul>
    <li><strong>Vaya primero a una reunión.</strong> Verá lo que la junta hace en realidad y cuánto hay que leer. El <a href="../">calendario</a> muestra muchas de ellas.</li>
    <li><strong>Conozca las reglas que tendría que seguir.</strong> Los miembros de las juntas están sujetos a las leyes de Idaho sobre reuniones abiertas, registros públicos y ética. No puede decidir asuntos en los que tenga un interés económico.</li>
    <li><strong>No necesita ser experto.</strong> La mayoría de las juntas quieren residentes que asistan, lean los documentos de la reunión y hagan buenas preguntas.</li>
  </ul>
""",
    sources=[("https://gov.idaho.gov/appointments/", "Nombramientos: la lista de juntas y la solicitud, Oficina del Gobernador (en inglés)"),
             ("https://gov.idaho.gov/appointment-vacancies/", "Vacantes para nombramientos, Oficina del Gobernador (en inglés)"),
             ("https://legislature.idaho.gov/statutesrules/idstat/Title74/T74CH2/", "Código de Idaho, Título 74, Capítulo 2: Ley de Reuniones Abiertas, Legislatura de Idaho (en inglés)")])

G["campaign-finance"] = dict(
    cat="Estado", title="Cómo seguir el dinero en la política de Idaho",
    lede="La Ley Sunshine (Sunshine Law) de Idaho obliga a los candidatos, a los comités políticos y a los cabilderos a reportar de dónde viene su dinero y a dónde va. Todo se puede buscar en línea.",
    body="""
  <h2>Quién reporta, y a quién</h2>
  <ul>
    <li><strong>Una sola oficina para todo.</strong> Desde 2020, el financiamiento de campañas en todos los niveles en Idaho, desde la junta escolar hasta el Gobernador, se reporta a la Secretaría de Estado de Idaho (Secretary of State).</li>
    <li><strong>Los candidatos</strong> reportan cada contribución y cada gasto, incluso su propio dinero.</li>
    <li><strong>Los comités políticos</strong> (PACs) y los grupos que hacen gastos independientes también reportan.</li>
    <li><strong>Los cabilderos</strong> se registran con la Secretaría de Estado y reportan lo que gastan.</li>
    <li><strong>Los candidatos al Congreso y a la Presidencia</strong> reportan en cambio a la Comisión Federal de Elecciones (Federal Election Commission, FEC).</li>
  </ul>

  <h2>Dónde buscar</h2>
  <ul>
    <li><strong>El Sunshine Portal</strong> tiene los reportes de 2023 en adelante: busque por candidato, comité o donante.</li>
    <li><strong>El sitio Sunshine anterior</strong> tiene de 2020 a 2023, incluidos los candidatos locales de esos años.</li>
    <li><strong>Un archivo de datos</strong> cubre de 2000 a 2019 para las contiendas estatales. Los registros locales de antes de 2020 los tiene el secretario (clerk) del condado o de la ciudad.</li>
    <li><strong>FEC.gov</strong> tiene a los candidatos federales.</li>
  </ul>

  <h2>Los límites</h2>
  <p>Una persona, una empresa o un comité político puede darle a un candidato, por elección:</p>
  <ul>
    <li><strong>$5,000</strong> para un cargo estatal, como Gobernador.</li>
    <li><strong>$1,000</strong> para la Legislatura o un cargo judicial.</li>
  </ul>
  <p>La primaria y la elección general cuentan por separado. La Legislatura consideró subir estos límites en 2026, así que revise las guías actuales de la Secretaría de Estado antes de confiar en una cifra.</p>

  <h2>Cuándo salen los reportes</h2>
  <ul>
    <li><strong>Cada mes en un año electoral,</strong> con fecha límite el día 10.</li>
    <li><strong>Una vez al año en los demás años,</strong> con fecha límite el 10 de enero.</li>
    <li><strong>Dentro de 48 horas</strong> para cualquier contribución individual de $1,000 o más.</li>
  </ul>

  <h2>Qué buscar</h2>
  <ul>
    <li><strong>Quién da más,</strong> y si vive o está en el distrito.</li>
    <li><strong>El dinero de comités.</strong> Busque al comité mismo para ver quién lo financia.</li>
    <li><strong>Los gastos independientes.</strong> Los grupos pueden gastar para apoyar o atacar a un candidato sin darle dinero a la campaña. Ese gasto se reporta por separado y muchas veces es la cifra más grande.</li>
    <li><strong>Las fechas.</strong> Las contribuciones grandes de último momento aparecen en los reportes de 48 horas, no en los mensuales.</li>
  </ul>

  <h2>Si algo parece estar mal</h2>
  <p>Las quejas sobre los reportes de financiamiento de campañas van a la oficina del Secretario de Estado, que puede multar a quien presente tarde o incompleto y enviar las violaciones para que se hagan cumplir.</p>
""",
    sources=[("https://voteidaho.gov/campaign-finance-portal/", "Campaign Finance 101, con enlaces a cada sitio de búsqueda, Secretaría de Estado de Idaho (en inglés)"),
             ("https://sunshine.voteidaho.gov/", "Sunshine Portal, Secretaría de Estado de Idaho (en inglés)"),
             ("https://archive.voteidaho.gov/download/cf_guide_state.pdf", "Guía de financiamiento de campañas para candidatos a cargos estatales, Secretaría de Estado de Idaho (en inglés)"),
             ("https://ballotpedia.org/Campaign_finance_in_Idaho", "Financiamiento de campañas en Idaho, Ballotpedia (en inglés)"),
             ("https://www.fec.gov/", "Comisión Federal de Elecciones (FEC) (en inglés)")])

G["state-agencies"] = dict(
    cat="Estado", title="Qué agencia estatal hace qué",
    lede="Un directorio breve para las necesidades más comunes, y qué hacer cuando no le dan respuesta.",
    body="""
  <h2>Necesidades de todos los días</h2>
  <ul>
    <li><strong>Seguro de salud, ayuda para alimentos, manutención de hijos, protección de menores:</strong> <a href="https://healthandwelfare.idaho.gov/" rel="noopener">Department of Health and Welfare</a> (Departamento de Salud y Bienestar). Al marcar 2-1-1 llega a Idaho CareLine, que conecta a las personas con servicios de salud y servicios humanos en todo el estado.</li>
    <li><strong>Desempleo, búsqueda de trabajo, salarios no pagados:</strong> <a href="https://www.labor.idaho.gov/" rel="noopener">Department of Labor</a> (Departamento de Trabajo).</li>
    <li><strong>Licencias de manejo y registro de vehículos:</strong> <a href="https://itd.idaho.gov/" rel="noopener">Idaho Transportation Department</a> (Departamento de Transporte de Idaho) pone las reglas y ofrece servicios en línea. En persona, las licencias se tramitan en la oficina del alguacil (sheriff) del condado y el registro en la oficina del tasador (assessor) del condado.</li>
    <li><strong>Impuesto estatal sobre la renta, impuesto sobre las ventas, alivio del impuesto a la propiedad:</strong> <a href="https://tax.idaho.gov/" rel="noopener">State Tax Commission</a> (Comisión de Impuestos del Estado).</li>
    <li><strong>Estafas, malas prácticas de negocios, preguntas sobre reuniones abiertas y registros públicos:</strong> <a href="https://www.ag.idaho.gov/" rel="noopener">Attorney General</a> (Fiscal General).</li>
    <li><strong>Quejas sobre seguros:</strong> <a href="https://doi.idaho.gov/" rel="noopener">Department of Insurance</a> (Departamento de Seguros).</li>
    <li><strong>Licencias profesionales y de contratistas, y quejas sobre un profesional con licencia:</strong> <a href="https://dopl.idaho.gov/" rel="noopener">Division of Occupational and Professional Licenses</a> (División de Licencias Ocupacionales y Profesionales).</li>
    <li><strong>Discriminación en el trabajo, en la vivienda o en lugares públicos:</strong> <a href="https://humanrights.idaho.gov/" rel="noopener">Idaho Human Rights Commission</a> (Comisión de Derechos Humanos de Idaho).</li>
    <li><strong>Votación, elecciones, registros de negocios:</strong> <a href="https://voteidaho.gov/" rel="noopener">Secretary of State</a> (Secretaría de Estado de Idaho).</li>
  </ul>

  <h2>Tierra, agua y aire libre</h2>
  <ul>
    <li><strong>Licencias de caza y pesca, vida silvestre:</strong> <a href="https://idfg.idaho.gov/" rel="noopener">Department of Fish and Game</a> (Departamento de Pesca y Caza).</li>
    <li><strong>Parques estatales, calcomanías para botes y vehículos todoterreno:</strong> <a href="https://parksandrecreation.idaho.gov/" rel="noopener">Department of Parks and Recreation</a> (Departamento de Parques y Recreación).</li>
    <li><strong>Derechos de agua y pozos:</strong> <a href="https://idwr.idaho.gov/" rel="noopener">Department of Water Resources</a> (Departamento de Recursos Hídricos).</li>
    <li><strong>Calidad del aire y del agua, derrames:</strong> <a href="https://www.deq.idaho.gov/" rel="noopener">Department of Environmental Quality</a> (Departamento de Calidad Ambiental).</li>
    <li><strong>Tarifas de electricidad, gas y agua:</strong> <a href="https://puc.idaho.gov/" rel="noopener">Public Utilities Commission</a> (Comisión de Servicios Públicos), que recibe comentarios del público en los casos de tarifas.</li>
  </ul>
  <p>Cerca de dos tercios de Idaho son tierras federales. Los bosques nacionales, las tierras de la Oficina de Administración de Tierras (Bureau of Land Management) y los parques nacionales los manejan agencias federales, no el estado. Vea <a href="federal-agencies.html">cómo tratar con las agencias federales</a>.</p>

  <h2>Escuelas y seguridad pública</h2>
  <ul>
    <li><strong>Escuelas de kínder a 12.º grado:</strong> primero su distrito escolar local, y luego el <a href="https://www.sde.idaho.gov/" rel="noopener">State Department of Education</a> (Departamento de Educación del Estado).</li>
    <li><strong>Universidades y colegios comunitarios:</strong> la <a href="https://boardofed.idaho.gov/" rel="noopener">State Board of Education</a> (Junta de Educación del Estado).</li>
    <li><strong>Prisiones estatales, libertad a prueba y libertad condicional (probation y parole):</strong> <a href="https://www.idoc.idaho.gov/" rel="noopener">Department of Correction</a> (Departamento Correccional). Las cárceles del condado las maneja el alguacil.</li>
    <li><strong>Carreteras estatales y patrulla de caminos:</strong> el Departamento de Transporte y la <a href="https://isp.idaho.gov/" rel="noopener">Idaho State Police</a> (Policía Estatal de Idaho).</li>
  </ul>

  <h2>Cuando no avanza</h2>
  <ol>
    <li><strong>Pida hablar con un supervisor, y anote nombres y fechas por escrito.</strong></li>
    <li><strong>Use el proceso formal de la agencia.</strong> La mayoría de las decisiones sobre beneficios, licencias y permisos vienen con el derecho a apelar y una fecha límite. La fecha límite está en el aviso.</li>
    <li><strong>Llame a sus legisladores.</strong> Ellos pueden preguntarle a una agencia por el caso de un constituyente. Vea <a href="../reps.html">Quién le representa</a>.</li>
    <li><strong>Comuníquese con la oficina del Gobernador,</strong> que recibe solicitudes de constituyentes sobre las agencias estatales.</li>
    <li><strong>Pida los registros.</strong> Puede pedir su propio expediente, o cualquier registro público, bajo la Ley de Registros Públicos (Public Records Act).</li>
  </ol>

  <h2>Reglas, no solo leyes</h2>
  <p>Las agencias escriben reglas que llenan los detalles de la ley estatal. Las reglas propuestas se publican en el Idaho Administrative Bulletin (Boletín Administrativo de Idaho), que sale cada mes, con un período de comentarios del público, y la Legislatura las revisa en cada sesión. Si el problema es una regla, ese período de comentarios es el momento para decirlo.</p>
""",
    sources=[("https://www.idaho.gov/", "Idaho.gov, el sitio web oficial del estado y su directorio de agencias (en inglés)"),
             ("https://gov.idaho.gov/contact/contact-us/", "Contacte a la oficina del Gobernador (en inglés)"),
             (PRM, "Manual de la Ley de Registros Públicos de Idaho, julio de 2026, Fiscal General de Idaho (en inglés)")])

G["running-for-office"] = dict(
    cat="Estado", title="Cómo postularse a un cargo público",
    lede="Idaho tiene miles de cargos electos, la mayoría locales y muchos sin competencia. Esto es qué cargos se eligen y cuándo, cómo se registra su candidatura y cuáles son las reglas sobre el dinero.",
    body="""
  <h2>Qué cargos se eligen y cuándo</h2>
  <ul>
    <li><strong>Años pares, con partido:</strong> los 105 escaños de la Legislatura, los comisionados del condado y otros funcionarios del condado, y los dos escaños de Idaho en la Cámara de Representantes de EE. UU. Las primarias de los partidos son el tercer martes de mayo y la elección general es en noviembre.</li>
    <li><strong>Cada cuatro años (2026, 2030):</strong> Gobernador, Vicegobernador (Lieutenant Governor), Secretario de Estado, Contralor (Controller), Tesorero (Treasurer), Fiscal General y Superintendente de Instrucción Pública (Superintendent of Public Instruction).</li>
    <li><strong>Años impares, sin partido:</strong> alcaldes, concejos municipales y miembros de juntas escolares (trustees), en noviembre.</li>
    <li><strong>Los jueces</strong> se postulan sin etiqueta de partido. Los jueces de la Corte Suprema, de la Corte de Apelaciones y de distrito aparecen en la boleta de mayo.</li>
    <li><strong>Los distritos especiales,</strong> como los de carreteras, bomberos, bibliotecas y cementerios, eligen a sus juntas en fechas de elección fijas en mayo o noviembre. El secretario (clerk) de su condado sabe cuáles.</li>
    <li><strong>Los delegados de precinto (precinct committeemen),</strong> el primer nivel de cargo dentro de un partido, se eligen en la primaria de mayo de los años pares. No hay cuota para registrarse.</li>
  </ul>

  <h2>Quién puede postularse</h2>
  <p>Para la mayoría de los cargos, debe ser un votante registrado que vive en el distrito que quiere representar. Algunos cargos tienen requisitos adicionales: los legisladores deben haber vivido en su distrito por un año, el Gobernador debe tener por lo menos 30 años, y los fiscales y jueces deben ser abogados. Las páginas para candidatos de la Secretaría de Estado de Idaho (Secretary of State), en inglés, explican las reglas de cada cargo.</p>
  <p>Un votante registrado es un ciudadano de EE. UU. de por lo menos 18 años que ha vivido en Idaho y en el condado por lo menos 30 días y se ha registrado (Código de Idaho § 34-402). Los residentes permanentes (green card) y otras personas que no son ciudadanas no pueden registrarse, así que no pueden votar, firmar peticiones ni postularse a estos cargos.</p>

  <h2>Registrar su candidatura</h2>
  <ul>
    <li><strong>Dónde:</strong> los candidatos a cargos federales, estatales, legislativos y judiciales se registran con el Secretario de Estado. Los candidatos del condado se registran con el secretario del condado, los de la ciudad con el secretario municipal, y los de distritos con el distrito o con el secretario del condado.</li>
    <li><strong>Cuándo:</strong> para la primaria de mayo, el período de registro dura unas dos semanas, a finales de febrero y principios de marzo. Los candidatos a la ciudad y a la junta escolar se registran a finales del verano de los años impares. Las fechas exactas se fijan en cada ciclo, y la fecha límite no se mueve.</li>
    <li><strong>Cuota o firmas:</strong> para la mayoría de los cargos con partido, puede pagar una cuota de registro o entregar firmas en una petición. En 2026 la cuota fue de $30 para la Legislatura y $40 para comisionado del condado, o 50 y 5 firmas. Los candidatos independientes deben registrarse por petición.</li>
    <li><strong>Los candidatos no inscritos en la boleta, cuyo nombre el votante escribe a mano (write-in),</strong> deben presentar una declaración de intención, o sus votos no se cuentan.</li>
  </ul>

  <h2>Las primarias de los partidos</h2>
  <p>Cada partido decide quién puede votar en su primaria. La primaria republicana está abierta solo a votantes registrados como republicanos, y en la mayor parte de Idaho la primaria republicana decide la elección. Si quiere tener voz en ella, revise su registro con mucha anticipación. La fecha límite para cambiarse de un partido a otro llega meses antes de la primaria de mayo, cuando cierra el registro de candidatos.</p>

  <h2>El dinero</h2>
  <ul>
    <li><strong>Lleve cuenta de todo desde el primer día,</strong> incluido su propio dinero.</li>
    <li><strong>Nombre a un tesorero de campaña (political treasurer) antes de recibir o gastar dinero.</strong> Todo candidato debe nombrar a un tesorero y darle el nombre y la dirección del tesorero a la Secretaría de Estado antes de recibir una contribución o hacer un gasto (Código de Idaho § 67-6603). Usted puede ser su propio tesorero.</li>
    <li><strong>Abra una cuenta bancaria aparte para la campaña.</strong> Desde el 1 de julio de 2026 (proyecto de ley H 930), el dinero de la campaña tiene que estar en su propia cuenta de cheques y no se puede mezclar con ningún otro dinero. Si usted le presta a su campaña más de $1,000 de su propio dinero, el préstamo tiene que depositarse en esa cuenta y reportarse. El dinero de la campaña solo se puede invertir en cuentas de efectivo, como certificados de depósito (CDs) o cuentas del mercado monetario (money market), no en acciones.</li>
    <li><strong>Sepa cuándo empiezan los informes.</strong> Los candidatos a cargos judiciales y locales no tienen que presentar informes hasta que recauden o gasten $500 (Código de Idaho § 67-6608). Los demás candidatos no tienen ese mínimo. Un grupo que recibe y gasta más de $1,000 en un año para apoyar o atacar a candidatos o medidas es un comité político, con su propio tesorero y sus propios informes (Código de Idaho § 67-6602).</li>
    <li><strong>Presente sus informes en línea</strong> en el Sunshine Portal de la Secretaría de Estado (en inglés), para cargos de cualquier nivel.</li>
    <li><strong>Conozca los límites.</strong> Las guías de la Secretaría de Estado indican $1,000 por donante por elección para cargos legislativos y $5,000 para cargos estatales. Confirme las cifras actuales antes de recaudar dinero.</li>
  </ul>
  <p>Vea <a href="campaign-finance.html">cómo seguir el dinero en la política de Idaho</a>.</p>

  <h2>Por dónde empezar</h2>
  <ul>
    <li><strong>Llame a la oficina de elecciones del secretario de su condado.</strong> Le dirán qué cargos se eligen, cuándo abre el registro y qué formularios necesita. Puede pedir un intérprete si lo necesita.</li>
    <li><strong>Vaya a las reuniones</strong> de la junta a la que quiere entrar. El <a href="../">calendario</a> muestra muchas de ellas.</li>
    <li><strong>Considere primero un cargo por nombramiento.</strong> Vea <a href="boards-and-commissions.html">cómo servir en una junta o comisión</a>.</li>
  </ul>
""",
    sources=[("https://voteidaho.gov/?p=2486", "Cómo postularse a un cargo, con cuotas y número de firmas para cada cargo, Secretaría de Estado de Idaho (en inglés)"),
             ("https://voteidaho.gov/candidate-filing/", "Registro de candidatos, Secretaría de Estado de Idaho (en inglés)"),
             ("https://voteidaho.gov/county-clerk/", "Oficinas de elecciones de los condados, Secretaría de Estado de Idaho (en inglés)"),
             ("https://archive.voteidaho.gov/download/cf_guide_local.pdf", "Guía de finanzas de campaña para candidatos a cargos locales, Secretaría de Estado de Idaho (en inglés)"),
             ("https://legislature.idaho.gov/statutesrules/idstat/Title67/T67CH66/SECT67-6603/", "Código de Idaho § 67-6603, el tesorero de campaña, Legislatura de Idaho (en inglés)"),
             ("https://legislature.idaho.gov/statutesrules/idstat/Title67/T67CH66/SECT67-6608/", "Código de Idaho § 67-6608, el mínimo de $500 para candidatos judiciales y locales, Legislatura de Idaho (en inglés)"),
             ("https://legislature.idaho.gov/sessioninfo/2026/legislation/H0930", "Proyecto de ley H 930 (2026), cuentas de campaña y préstamos del candidato, Legislatura de Idaho (en inglés)"),
             ("https://sunshine.voteidaho.gov/", "Sunshine Portal, Secretaría de Estado de Idaho (en inglés)")])

G["state-initiatives"] = dict(
    cat="Estado", title="Iniciativas y referendos estatales",
    lede="Los votantes de Idaho pueden escribir leyes estatales ellos mismos y pueden anular leyes que aprueba la Legislatura. Las reglas sobre firmas están entre las más estrictas del Oeste. Así funciona cada camino.",
    body="""
  <h2>Dos caminos para los votantes</h2>
  <ul>
    <li><strong>Iniciativa.</strong> Los votantes proponen una ley nueva o un cambio a una ley existente. Con suficientes firmas, va a la boleta de noviembre de un año par.</li>
    <li><strong>Referendo.</strong> Los votantes piden anular una ley que la Legislatura acaba de aprobar. La petición tiene que presentarse dentro de los 60 días después de que termina la sesión legislativa.</li>
  </ul>
  <p>En Idaho, las iniciativas solo pueden cambiar la ley estatal. Los votantes no pueden proponer enmiendas a la Constitución de Idaho. Esas tienen que venir de la Legislatura.</p>

  <h2>Cuántas firmas</h2>
  <ul>
    <li><strong>El seis por ciento de los votantes registrados en todo el estado,</strong> contados a la fecha de la última elección general.</li>
    <li><strong>Y el seis por ciento en cada uno de por lo menos 18 de los 35 distritos legislativos.</strong> Las firmas de Boise solas no bastan para que una medida llegue a la boleta.</li>
  </ul>
  <p>La Secretaría de Estado de Idaho (Secretary of State) publica las cifras exactas de cada ciclo. Las campañas juntan mucho más que el mínimo, porque los secretarios (clerks) de los condados descartan las firmas que no coinciden con un votante registrado en esa dirección.</p>

  <h2>Los pasos</h2>
  <ol class="steps">
    <li><strong>Empezar con 20 firmas.</strong> Los patrocinadores presentan el texto propuesto ante el Secretario de Estado, junto con las firmas de 20 votantes registrados y una propuesta de cómo pagar por la medida.</li>
    <li><strong>Revisión.</strong> El Fiscal General (Attorney General) revisa el texto y puede sugerir cambios, que los patrocinadores pueden ignorar. La oficina de presupuesto del estado escribe una declaración de impacto fiscal.</li>
    <li><strong>Títulos de la boleta.</strong> El Fiscal General escribe un título corto y uno largo. Cualquier persona que no esté de acuerdo con ellos puede apelar ante la Corte Suprema de Idaho dentro de 20 días.</li>
    <li><strong>Recolección de firmas.</strong> Los patrocinadores tienen hasta 18 meses, que terminan el 30 de abril del año de la elección. Quienes recolectan firmas deben vivir en Idaho y tener por lo menos 18 años, y cada hoja de firmas es para un solo condado.</li>
    <li><strong>Los secretarios de los condados verifican.</strong> Las firmas se entregan a los secretarios de los condados a más tardar el 1 de mayo, y ellos tienen hasta finales de junio para revisarlas.</li>
    <li><strong>La boleta.</strong> Una medida con suficientes firmas válidas va a la boleta de noviembre y se aprueba con mayoría simple.</li>
  </ol>

  <h2>Si le piden que firme</h2>
  <ul>
    <li><strong>Puede leerla primero.</strong> La persona que recolecta firmas debe mostrarle los títulos de la boleta y ofrecerle una copia de la medida y del resumen de su impacto fiscal.</li>
    <li><strong>Debe ser un votante calificado:</strong> ciudadano de EE. UU., de por lo menos 18 años, que ha vivido en Idaho y en su condado por lo menos 30 días y está registrado para votar (Código de Idaho § 34-402). Los residentes permanentes (green card) y otras personas que no son ciudadanas no pueden firmar. Usted firma con su propio nombre y dirección.</li>
    <li><strong>Puede cambiar de opinión.</strong> Puede quitar su nombre antes de que la petición llegue al secretario del condado, o pedírselo por escrito al secretario antes de que se verifiquen las firmas.</li>
    <li><strong>Firmar no es votar.</strong> Solo dice que la pregunta debe estar en la boleta.</li>
  </ul>

  <h2>Después de que se aprueba una iniciativa</h2>
  <p>Una ley aprobada por iniciativa es una ley estatal común. La Legislatura puede enmendarla o derogarla en cualquier momento con mayoría simple, y lo ha hecho.</p>

  <h2>Medidas que la Legislatura le envía</h2>
  <ul>
    <li><strong>Enmiendas a la Constitución.</strong> Necesitan el voto de dos tercios tanto en la Cámara de Representantes como en el Senado, y luego la mayoría de los votantes en la siguiente elección general.</li>
    <li><strong>Preguntas consultivas.</strong> A veces la Legislatura hace a los votantes una pregunta que no es obligatoria.</li>
  </ul>

  <h2>Cómo participar</h2>
  <ul>
    <li><strong>Lea el folleto para votantes (voters' pamphlet)</strong> que la Secretaría de Estado envía por correo antes de la elección general, con el texto de cada medida y los argumentos a favor y en contra.</li>
    <li><strong>Revise quién financia cada lado</strong> en el <a href="campaign-finance.html">Sunshine Portal</a>.</li>
  </ul>
""",
    sources=[("https://voteidaho.gov/initiative-filing-requirements/", "Requisitos para presentar una iniciativa, Secretaría de Estado de Idaho (en inglés)"),
             ("https://voteidaho.gov/?p=3109", "Iniciativas y enmiendas, actuales y pasadas, Secretaría de Estado de Idaho (en inglés)"),
             ("https://legislature.idaho.gov/statutesrules/idstat/", "Código de Idaho, Título 34, Capítulo 18: Elecciones de iniciativa y referendo, Legislatura de Idaho (en inglés)"),
             ("https://legislature.idaho.gov/statutesrules/idstat/title34/t34ch4/sect34-402", "Código de Idaho § 34-402, quién puede votar, Legislatura de Idaho (en inglés)"),
             ("https://legislature.idaho.gov/statutesrules/idconst/", "Constitución de Idaho, Artículo III, Sección 1 y Artículo XX, Legislatura de Idaho (en inglés)")])

G["federal-offices"] = dict(
    cat="Federal", title="Las elecciones federales y quién puede postularse",
    lede="Idaho envía a cuatro personas al Congreso y ayuda a elegir al Presidente. Esto es quién puede postularse a cada cargo y cada cuánto se elige.",
    body="""
  <h2>Los cargos</h2>
  <ul>
    <li><strong>Cámara de Representantes de EE. UU.</strong> Idaho tiene dos miembros en la Cámara, cada uno elegido por un distrito del Congreso para un período de dos años. El Distrito 1 cubre el norte y el oeste, incluidos el Panhandle y el condado de Canyon. El Distrito 2 cubre el este y el sur, incluida la mayor parte de Boise. Los dos escaños están en la boleta cada año par.</li>
    <li><strong>Senado de EE. UU.</strong> Idaho tiene dos senadores, elegidos en todo el estado para períodos de seis años. Sus períodos están escalonados, así que los escaños se eligen en años diferentes.</li>
    <li><strong>Presidente y Vicepresidente.</strong> Se eligen cada cuatro años. Idaho tiene cuatro votos electorales, y los cuatro van a la fórmula que gana el voto popular en el estado.</li>
  </ul>

  <h2>Quién puede postularse (según la Constitución de EE. UU.)</h2>
  <ul>
    <li><strong>Cámara:</strong> tener por lo menos 25 años, ser ciudadano de EE. UU. desde hace por lo menos siete años y vivir en el estado. Los miembros no tienen que vivir en el distrito que representan.</li>
    <li><strong>Senado:</strong> tener por lo menos 30 años, ser ciudadano de EE. UU. desde hace por lo menos nueve años y vivir en el estado.</li>
    <li><strong>Presidente:</strong> tener por lo menos 35 años, ser ciudadano por nacimiento (natural-born citizen) y haber vivido en EE. UU. por lo menos 14 años. Nadie puede ser elegido Presidente más de dos veces.</li>
  </ul>

  <h2>Cómo organiza Idaho estas elecciones</h2>
  <ul>
    <li><strong>Los candidatos a la Cámara y al Senado</strong> se nominan en las primarias de los partidos, el tercer martes de mayo. Cada partido decide quién puede votar en su primaria, y la primaria republicana está abierta solo a republicanos registrados. Los ganadores se enfrentan en noviembre.</li>
    <li><strong>Las nominaciones presidenciales</strong> las organizan los partidos. En 2024 Idaho no tuvo una primaria presidencial organizada por el estado, y los dos partidos principales usaron asambleas (caucuses). Consulte con su partido o con la Secretaría de Estado de Idaho (Secretary of State) cómo será en 2028.</li>
    <li><strong>Los candidatos al Congreso</strong> se registran con el Secretario de Estado de Idaho durante el período de registro de finales del invierno. En 2026 la cuota fue de $500 para el Senado y $300 para la Cámara, o firmas en una petición en su lugar. Informan el dinero de su campaña a la Comisión Federal de Elecciones (Federal Election Commission), no al estado.</li>
  </ul>

  <h2>Cómo seguir a sus miembros del Congreso</h2>
  <ul>
    <li><strong>Encuéntrelos</strong> con <a href="../reps.html">Quién le representa</a>.</li>
    <li><strong>Siga sus votos y proyectos de ley</strong> en Congress.gov (en inglés).</li>
    <li><strong>Vea quién financia sus campañas</strong> en el sitio web de la Comisión Federal de Elecciones, fec.gov (en inglés).</li>
    <li><strong>Use sus oficinas en Idaho.</strong> Cada miembro tiene personal en varias ciudades de Idaho que ayuda con las agencias federales. Vea <a href="federal-agencies.html">cómo tratar con las agencias federales</a>.</li>
  </ul>
""",
    sources=[("https://constitution.congress.gov/constitution/", "La Constitución de los Estados Unidos, Congress.gov (en inglés)"),
             ("https://legislature.idaho.gov/legislators/congressional-delegation/", "La delegación de Idaho en el Congreso, Legislatura de Idaho (en inglés)"),
             ("https://voteidaho.gov/?p=2486", "Cómo postularse a un cargo, Secretaría de Estado de Idaho (en inglés)"),
             ("https://www.congress.gov/", "Congress.gov (en inglés)"),
             ("https://www.fec.gov/", "Comisión Federal de Elecciones (en inglés)")])

G["courts"] = dict(
    cat="Federal y estatal", title="Cómo funcionan las cortes",
    lede="La mayoría de las personas tienen contacto con las cortes por una multa de tráfico, un asunto familiar, un reclamo menor o el servicio de jurado. Así están organizadas las cortes de Idaho y las cortes federales, una al lado de la otra.",
    body="""
  <h2>Las cortes estatales de Idaho</h2>
  <p>Idaho tiene un solo sistema de cortes unificado, dirigido por la Corte Suprema de Idaho, con un juzgado en cada condado. Casi todos los casos empiezan en una corte de distrito.</p>
  <ul>
    <li><strong>División de magistrados (magistrate division).</strong> Es parte de la corte de distrito, y es donde termina la mayoría de la gente. Los jueces magistrados atienden multas de tráfico e infracciones, delitos menores (misdemeanors), las primeras audiencias en casos de delitos graves (felonies), reclamos menores (small claims), casos civiles de hasta $10,000, desalojos, divorcios y custodia, casos de menores, sucesiones (probate) y tutelas (guardianships).</li>
    <li><strong>Jueces de distrito.</strong> Atienden los juicios por delitos graves, los casos civiles de más de $10,000 y las apelaciones de la división de magistrados. El estado está dividido en siete distritos judiciales.</li>
    <li><strong>Corte de Apelaciones (Court of Appeals).</strong> Cuatro jueces, en paneles de tres, atienden las apelaciones que la Corte Suprema les asigna. Revisan el expediente. No hay juicios nuevos ni testigos.</li>
    <li><strong>Corte Suprema (Supreme Court).</strong> Cinco jueces (justices). Tiene la última palabra sobre la ley de Idaho, y además escribe las reglas de las cortes y supervisa a los abogados.</li>
  </ul>

  <h2>Cómo llegan a su cargo los jueces de Idaho</h2>
  <ul>
    <li><strong>Los jueces de la Corte Suprema, los jueces de apelaciones y los jueces de distrito se eligen</strong> sin etiqueta de partido, en la boleta de mayo. Los períodos en la Corte Suprema y en la Corte de Apelaciones son de seis años, y los de los jueces de distrito son de cuatro.</li>
    <li><strong>En la práctica, la mayoría primero son nombrados.</strong> Cuando un juez deja el cargo antes de terminar su período, el Gobernador nombra a un reemplazo de una lista de candidatos, y ese juez luego se presenta a elección.</li>
    <li><strong>Los jueces magistrados son nombrados</strong> por una comisión en cada distrito judicial, y luego enfrentan una votación de sí o no para seguir en el cargo (retention vote).</li>
  </ul>

  <h2>Las cortes federales</h2>
  <ul>
    <li><strong>Corte de Distrito de EE. UU. para el Distrito de Idaho (U.S. District Court for the District of Idaho).</strong> Es la corte de primera instancia para delitos federales, casos bajo la ley federal o la Constitución de EE. UU., bancarrotas y algunas disputas entre personas de estados diferentes.</li>
    <li><strong>Corte de Apelaciones del Noveno Circuito (Ninth Circuit Court of Appeals).</strong> Atiende las apelaciones de Idaho y de otros ocho estados del Oeste.</li>
    <li><strong>Corte Suprema de EE. UU.</strong> Acepta una pequeña parte de los casos que le piden revisar.</li>
  </ul>
  <p>Los jueces federales son nominados por el Presidente, confirmados por el Senado y sirven de por vida.</p>

  <h2>Las cortes tribales</h2>
  <p>Las cinco tribus de Idaho reconocidas por el gobierno federal, Coeur d'Alene, Kootenai, Nez Perce, Shoshone-Bannock y Shoshone-Paiute, son gobiernos soberanos con sus propias cortes y leyes.</p>

  <h2>Cuál es su papel</h2>
  <ul>
    <li><strong>Observar.</strong> Las audiencias en las cortes están abiertas al público, con pocas excepciones, como los casos de menores.</li>
    <li><strong>Buscar un caso.</strong> El iCourt Portal de Idaho (en inglés) tiene los expedientes públicos de los casos de todos los condados.</li>
    <li><strong>Recibir ayuda sin abogado.</strong> La Court Assistance Office (Oficina de Asistencia de la Corte) ofrece formularios y orientación a las personas que se representan a sí mismas, con una oficina en la mayoría de los juzgados. Puede preguntar en la corte si hay un intérprete disponible.</li>
    <li><strong>Servir como jurado.</strong> Los nombres se sacan de las listas de registro de votantes y de licencias de manejo. Para ser jurado hay que ser ciudadano de EE. UU., tener por lo menos 18 años y vivir en el condado (Código de Idaho § 2-209). Como las listas de licencias de manejo incluyen a personas que no son ciudadanas, alguien que no es ciudadano puede recibir una citación. No la ignore: responda a la corte e indique que no es ciudadano de EE. UU. Su empleador no puede despedirle por servir.</li>
    <li><strong>Votar.</strong> Los jueces aparecen en su boleta. Las elecciones con más de un candidato son raras, y por eso las que hay importan más. Solo los ciudadanos de EE. UU. de 18 años o más que estén registrados pueden votar en Idaho (Código de Idaho § 34-402).</li>
  </ul>
""",
    sources=[("https://isc.idaho.gov/about-the-courts", "Acerca de las cortes, Corte Suprema de Idaho (en inglés)"),
             ("https://archive.sos.idaho.gov/blue_book/blue_book_2025-2026.pdf", "The Blue Book of Idaho, 2025-2026, sección del poder judicial, Secretaría de Estado de Idaho (en inglés)"),
             ("https://courtselfhelp.idaho.gov/", "Court Assistance Office (Oficina de Asistencia de la Corte), Corte Suprema de Idaho (en inglés)"),
             ("https://legislature.idaho.gov/statutesrules/idstat/Title2/T2CH2/SECT2-209", "Código de Idaho § 2-209, requisitos para ser jurado, Legislatura de Idaho (en inglés)"),
             ("https://www.uscourts.gov/about-federal-courts", "Acerca de las cortes federales, United States Courts (en inglés)")])

G["constitution"] = dict(
    cat="Federal y estatal", title="Cómo entender la Constitución",
    lede="Usted vive bajo dos constituciones: la Constitución de los Estados Unidos y la de Idaho. Esto es lo que hace cada una y cómo cambia cada una.",
    body="""
  <h2>La Constitución de EE. UU.</h2>
  <ul>
    <li><strong>Establece el gobierno federal:</strong> el Congreso, el Presidente y las cortes federales, y cada uno pone límites a los otros.</li>
    <li><strong>Divide el poder</strong> entre el gobierno federal y los estados.</li>
    <li><strong>Protege los derechos individuales,</strong> sobre todo por medio de sus enmiendas. Las primeras diez son la Carta de Derechos (Bill of Rights). Las posteriores acabaron con la esclavitud, garantizaron la igual protección ante la ley y el debido proceso, y ampliaron el derecho al voto.</li>
  </ul>

  <h2>La Constitución de Idaho</h2>
  <ul>
    <li><strong>Viene de cuando Idaho se convirtió en estado.</strong> Los delegados la escribieron en Boise en el verano de 1889, los votantes la aprobaron ese otoño, e Idaho se convirtió en estado el 3 de julio de 1890.</li>
    <li><strong>Es más larga y más específica</strong> que la federal. Trata sobre las escuelas, los derechos de agua, los impuestos, las tierras públicas, los condados y las ciudades.</li>
    <li><strong>El Artículo I es la declaración de derechos propia de Idaho.</strong> Las constituciones estatales pueden proteger más que la federal, y la de Idaho incluye derechos que la Constitución federal no menciona de forma expresa, como los derechos de las víctimas de delitos y el derecho a cazar, pescar y poner trampas.</li>
    <li><strong>Limita al gobierno de maneras prácticas:</strong> el presupuesto tiene que estar equilibrado, la mayoría de las deudas de los gobiernos locales necesitan el voto de dos tercios de los votantes, y la Legislatura tiene que mantener un sistema de escuelas públicas gratuitas "general, uniforme y completo" ("general, uniform and thorough").</li>
    <li><strong>Reserva poder a los votantes:</strong> la iniciativa, el referendo y la revocación de mandato (recall) están todos en la constitución.</li>
  </ul>

  <h2>Cómo cambia cada una</h2>
  <ul>
    <li><strong>Constitución de EE. UU.:</strong> una enmienda necesita dos tercios de ambas cámaras del Congreso, y luego la aprobación de tres cuartas partes de los estados. Se ha enmendado 27 veces.</li>
    <li><strong>Constitución de Idaho:</strong> una enmienda necesita dos tercios tanto de la Cámara de Representantes como del Senado, y luego la mayoría de los votantes en la siguiente elección general. Los votantes no pueden proponer enmiendas por iniciativa.</li>
  </ul>
  <p>Eso significa que cada cambio a la constitución de Idaho le llega a usted como una pregunta en la boleta, por lo general marcada como HJR o SJR con un número. Vea <a href="state-initiatives.html">iniciativas y referendos estatales</a>.</p>

  <h2>Quién decide lo que significa</h2>
  <p>Las cortes, caso por caso. La Corte Suprema de EE. UU. tiene la última palabra sobre la Constitución federal, y la Corte Suprema de Idaho tiene la última palabra sobre la de Idaho. Vea <a href="courts.html">cómo funcionan las cortes</a>.</p>

  <h2>Léalas usted mismo</h2>
  <p>Las dos son lo bastante cortas para leerlas en una tarde. El sitio web de la Legislatura tiene la Constitución de Idaho completa, artículo por artículo, y Congress.gov tiene la Constitución de EE. UU. con notas en lenguaje sencillo sobre cada cláusula. Ambos sitios están en inglés.</p>
""",
    sources=[("https://legislature.idaho.gov/statutesrules/idconst/", "Constitución del Estado de Idaho, Legislatura de Idaho (en inglés)"),
             ("https://constitution.congress.gov/constitution/", "La Constitución de los Estados Unidos, con notas, Congress.gov (en inglés)"),
             ("https://www.archives.gov/espanol/constitucion", "La Constitución de los Estados Unidos, Archivos Nacionales (en español)")])

G["federal-agencies"] = dict(
    cat="Federal", title="Cómo tratar con las agencias federales",
    lede="Cuando un trámite con una agencia federal está detenido, va lento o la agencia está por tomar una decisión que le afecta, hay maneras de avanzar. En Idaho, donde el gobierno federal administra la mayor parte de la tierra, esto pasa a menudo.",
    body="""
  <h2>Cuando su trámite con una agencia está detenido</h2>
  <p><strong>Pida ayuda a su miembro del Congreso.</strong> Cada oficina de la Cámara de Representantes y del Senado tiene personal que ayuda a los constituyentes con las agencias federales, incluidos el Seguro Social, Medicare, los beneficios para veteranos, el IRS, los pasaportes y los casos de inmigración.</p>
  <ul>
    <li><strong>Llame o llene el formulario en línea de la oficina.</strong> Encuentre a sus miembros con <a href="../reps.html">Quién le representa</a>. Cada uno tiene oficinas en distintas partes de Idaho.</li>
    <li><strong>Prepárese para firmar una autorización de privacidad (privacy release),</strong> que permite que la agencia comparta su caso con la oficina.</li>
    <li><strong>Lleve los números de caso y copias de las cartas.</strong></li>
  </ul>

  <h2>Decisiones sobre tierras públicas</h2>
  <p>El Servicio Forestal (Forest Service) y la Oficina de Administración de Tierras (Bureau of Land Management, BLM) administran la mayor parte de la tierra de Idaho. Los permisos de pastoreo, las ventas de madera, los planes de caminos y uso de vehículos, la minería y los proyectos contra incendios pasan por revisión pública.</p>
  <ul>
    <li><strong>Cada bosque nacional y cada distrito del BLM publica sus proyectos</strong> y recibe comentarios, por lo general durante 30 días o más.</li>
    <li><strong>Inscríbase en la lista de correo</strong> del bosque o del distrito cercano a usted, para que los avisos le lleguen mientras el período de comentarios está abierto.</li>
    <li><strong>Comente temprano y con detalle.</strong> En muchos proyectos, solo las personas que comentaron pueden presentar una objeción después.</li>
    <li><strong>Los grupos asesores locales,</strong> como los consejos asesores de recursos del BLM (resource advisory councils), tienen lugares para residentes.</li>
  </ul>

  <h2>Comente sobre una regla propuesta</h2>
  <p>Las agencias federales escriben reglamentos para aplicar las leyes. Antes de que la mayoría de las reglas sean finales, la agencia publica una propuesta y recibe comentarios del público.</p>
  <ul>
    <li><strong>Busque las reglas propuestas</strong> en el Registro Federal (Federal Register).</li>
    <li><strong>Comente en Regulations.gov</strong> antes de la fecha límite. El sitio está en inglés.</li>
    <li><strong>Sea específico.</strong> Las agencias tienen que considerar el contenido de los comentarios, no contarlos. Explique cómo le afectaría la regla y sugiera un cambio.</li>
  </ul>

  <h2>Pida registros</h2>
  <p>La Ley de Libertad de Información (Freedom of Information Act, FOIA) permite que cualquier persona pida registros a las agencias federales. FOIA.gov explica cómo hacerlo y tiene enlaces a la página de solicitudes de cada agencia. Algunos registros están exentos, como la información clasificada y los datos personales privados.</p>

  <h2>Reporte un problema</h2>
  <ul>
    <li><strong>La mayoría de las agencias tienen un Inspector General</strong> que investiga el fraude, el desperdicio y el abuso, y recibe denuncias del público.</li>
    <li><strong>Muchas agencias también tienen un defensor (ombudsman)</strong> que ayuda a resolver quejas.</li>
  </ul>
""",
    sources=[("https://www.regulations.gov/", "Regulations.gov (en inglés)"),
             ("https://www.federalregister.gov/", "Registro Federal (Federal Register) (en inglés)"),
             ("https://www.foia.gov/", "FOIA.gov (en inglés)"),
             ("https://legislature.idaho.gov/legislators/congressional-delegation/", "La delegación de Idaho en el Congreso, Legislatura de Idaho (en inglés)")])

G["federal-budget"] = dict(
    cat="Federal", title="El presupuesto federal y dónde puede opinar",
    lede="El presupuesto federal paga cosas de las que Idaho depende, desde los bosques nacionales y las carreteras hasta la atención a veteranos y el Laboratorio Nacional de Idaho (Idaho National Laboratory). Así se hace y aquí es donde cabe la participación del público.",
    body="""
  <h2>Dos tipos de gasto</h2>
  <ul>
    <li><strong>El gasto obligatorio (mandatory spending)</strong> lo fijan leyes que ya existen y no necesita un voto cada año. Incluye el Seguro Social, Medicare y la mayor parte de Medicaid. Es la parte más grande.</li>
    <li><strong>El gasto discrecional (discretionary spending)</strong> lo decide el Congreso cada año por medio de proyectos de ley de asignaciones presupuestarias (appropriations bills). Cubre la defensa y la mayoría de las agencias, subvenciones y programas federales.</li>
  </ul>

  <h2>El ciclo anual</h2>
  <ul>
    <li><strong>El año fiscal</strong> va del 1 de octubre al 30 de septiembre.</li>
    <li><strong>A principios del año,</strong> el Presidente envía al Congreso una solicitud de presupuesto. Es una propuesta, no una ley.</li>
    <li><strong>Primavera y verano:</strong> los subcomités de asignaciones de la Cámara de Representantes y del Senado escriben los proyectos de ley de gasto anual, por lo general 12, cada uno para un grupo de agencias.</li>
    <li><strong>Para el 1 de octubre,</strong> el Congreso debería aprobarlos. Cuando no lo hace, por lo general aprueba una resolución de continuidad (continuing resolution) para mantener los fondos a los niveles actuales. Si no se aprueba ninguna de las dos cosas, partes del gobierno cierran.</li>
  </ul>

  <h2>Dónde puede opinar</h2>
  <ul>
    <li><strong>Comuníquese con sus miembros del Congreso</strong> sobre los programas que le importan, sobre todo en la primavera, mientras se escriben los proyectos de ley de asignaciones.</li>
    <li><strong>Proyectos locales.</strong> Los miembros del Congreso pueden pedir fondos para proyectos comunitarios específicos en su distrito o estado. Los gobiernos locales, las organizaciones sin fines de lucro y las tribus se los piden a sus miembros, por lo general a finales del invierno o principios de la primavera. Revise los sitios web de sus miembros para conocer su proceso y sus fechas límite.</li>
    <li><strong>Testimonio de testigos del público.</strong> Algunos subcomités de asignaciones aceptan testimonio por escrito del público.</li>
    <li><strong>El dinero federal a menudo pasa por el estado.</strong> Medicaid, los fondos para carreteras y muchas subvenciones pasan por agencias de Idaho, y la Legislatura decide si se gastan y cómo. Vea <a href="state-budgets.html">el presupuesto estatal y cómo influir en él</a>.</li>
  </ul>

  <h2>Cómo seguir el dinero</h2>
  <p>La Oficina de Presupuesto del Congreso (Congressional Budget Office) publica resúmenes del presupuesto en lenguaje sencillo, y USAspending.gov muestra adónde va el dinero federal, hasta el nivel del condado. Ambos están en inglés.</p>
""",
    sources=[("https://www.cbo.gov/topics/budget", "El presupuesto federal, Oficina de Presupuesto del Congreso (en inglés)"),
             ("https://www.usaspending.gov/", "USAspending.gov (en inglés)"),
             ("https://www.congress.gov/", "Congress.gov (en inglés)")])
