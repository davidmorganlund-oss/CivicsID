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
    <li><strong>Recibe aviso.</strong> Una reunión ordinaria requiere por lo menos cinco días naturales de aviso y una agenda publicada con 48 horas de anticipación. Una reunión especial requiere 24 horas de aviso de ambas cosas (§ 74-204).</li>
    <li><strong>La agenda tiene que ser real.</strong> En general, el órgano solo puede decidir lo que está en la agenda, y los asuntos que se votarán deben marcarse como "action items" (puntos de acción).</li>
    <li><strong>Las sesiones a puerta cerrada son limitadas.</strong> Solo se permiten por razones que la ley enumera, como contratar personal, la disciplina de un empleado específico, comprar terrenos o demandas pendientes. Requieren un voto nominal de dos tercios, y no se puede tomar ninguna decisión final a puerta cerrada (§ 74-206).</li>
    <li><strong>Hay actas.</strong> Las actas escritas deben registrar quién estuvo presente, cada moción y cada votación, y estar disponibles al público (§ 74-205).</li>
    <li><strong>Puede grabar.</strong> Puede grabar audio o video de una reunión abierta, y no lo pueden sacar por hacerlo (§ 74-203(6)).</li>
  </ul>

  <h2>Lo que no le garantiza</h2>
  <p><strong>La Ley de Reuniones Abiertas le da el derecho a observar, no el derecho a hablar.</strong> Un órgano no está obligado a recibir comentarios del público en una reunión ordinaria. La mayoría de los concejos municipales y juntas escolares lo hacen por decisión propia, según sus propias reglas.</p>
  <p><strong>Las audiencias públicas son diferentes.</strong> Cuando una ley exige una audiencia, el órgano debe dejar que la gente testifique. Eso incluye el presupuesto anual, la mayoría de las decisiones de zonificación y uso de suelo, y muchos aumentos de tarifas. Si quiere asegurarse de ser escuchado, una audiencia pública es el lugar.</p>

  <h2>Antes de la reunión</h2>
  <ol>
    <li><strong>Encuentre la reunión.</strong> El <a href="../index.html">calendario</a> muestra lo que viene cerca de usted.</li>
    <li><strong>Lea la agenda.</strong> Busque el asunto que le interesa y anote su número o título, y si es un punto de acción o una audiencia pública. Casi todas las agendas están en inglés; puede pedirle ayuda al secretario (clerk).</li>
    <li><strong>Averigüe cómo recibe comentarios ese órgano.</strong> Cada uno pone sus propias reglas: si hay que inscribirse antes o en la puerta, cuánto tiempo le dan y si puede hablar por teléfono o video. Llame al secretario si el sitio web no lo dice.</li>
    <li><strong>Pida un intérprete con tiempo.</strong> Muchas ciudades y condados ofrecen interpretación si se pide con anticipación. Pregunte al secretario unos días antes.</li>
    <li><strong>Si no hay período de comentarios,</strong> envíe un correo a los miembros antes de la reunión.</li>
  </ol>

  <h2>Qué decir</h2>
  <p>El tiempo suele ser corto, a menudo dos o tres minutos, así que escríbalo y mida el tiempo.</p>
  <ol>
    <li><strong>Quién es usted.</strong> Su nombre y que vive, trabaja o tiene un negocio en la comunidad.</li>
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

  <p>Si un órgano no cumple con la ley, vea <a href="open-meeting-law.html">la Ley de Reuniones Abiertas de Idaho</a>.</p>
""",
    sources=[("https://legislature.idaho.gov/statutesrules/idstat/Title74/T74CH2/", "Código de Idaho, Título 74, Capítulo 2: Ley de Reuniones Abiertas (en inglés)"),
             (OML, "Manual de la Ley de Reuniones Abiertas de Idaho, julio de 2026, Fiscal General (en inglés)")])

G["open-meeting-law"] = dict(
    cat="Local", title="La Ley de Reuniones Abiertas de Idaho: qué exige",
    lede="Cuando un concejo municipal, una comisión del condado, una junta escolar u otro órgano público se reúne para decidir o discutir asuntos públicos, la ley de Idaho dice que el público tiene derecho a verlo. Esto es lo que garantiza, lo que no, y qué puede hacer cuando un órgano no cumple.",
    body="""
  <h2>A quién se aplica</h2>
  <p>La ley se aplica a los órganos de gobierno de agencias estatales y locales: concejos municipales, comisiones de condado, juntas escolares, juntas de bibliotecas y de distritos de carreteras, y las comisiones y comités que toman decisiones o hacen recomendaciones (Código de Idaho §§ 74-202(4)&ndash;(5)). No se aplica a los tribunales, a un funcionario que actúa solo, ni a grupos privados como organizaciones sin fines de lucro o asociaciones de propietarios.</p>
  <p>Una <strong>reunión</strong> es cualquier encuentro de un quórum para tomar una decisión o deliberar sobre ella, sea formal, informal o social (§ 74-202(6)). Los miembros no pueden evitar la ley reuniéndose en grupos más pequeños o pasando opiniones por medio de otra persona, y los intercambios por correo o mensajes de texto entre un quórum también pueden contar.</p>

  <h2>Aviso y agendas</h2>
  <ul>
    <li><strong>Reuniones ordinarias:</strong> por lo menos 5 días naturales de aviso de la reunión y 48 horas de aviso de la agenda (§ 74-204(1)). Los órganos que se reúnen al menos una vez al mes pueden publicar su calendario anual en su lugar.</li>
    <li><strong>Reuniones especiales:</strong> por lo menos 24 horas de aviso de la reunión y de la agenda (§ 74-204(2)). Las verdaderas emergencias son una excepción, y el órgano debe explicar la emergencia al inicio de la reunión.</li>
    <li>Los avisos se publican en la oficina de la agencia y en su sitio web o redes sociales, si los tiene.</li>
    <li>Las agendas deben indicar los temas específicos, y todo lo que se vaya a votar debe marcarse como <strong>punto de acción</strong> ("action item") (§ 74-204(4)).</li>
  </ul>

  <h2>Sesiones a puerta cerrada ("executive sessions")</h2>
  <p>Un órgano solo puede cerrar parte de una reunión por las razones que enumera el § 74-206(1), y se interpretan de manera estricta. Incluyen contratar, evaluar o disciplinar a un empleado específico; comprar una propiedad; hablar con su abogado sobre un litigio pendiente o probable; y registros que están exentos de divulgación.</p>
  <p>Para cerrar la sesión, el órgano debe votar con una <strong>mayoría de dos tercios en votación nominal</strong>, citando la razón específica. <strong>No se puede tomar ninguna decisión final a puerta cerrada</strong> (§ 74-206). La votación tiene que ser en público.</p>

  <h2>Sus derechos</h2>
  <ul>
    <li><strong>Asistir.</strong> Se permiten reglas para mantener el orden, pero no reglas que hagan imposible asistir.</li>
    <li><strong>Grabar.</strong> Puede grabar reuniones abiertas en audio, video o fotos, y no lo pueden sacar por hacerlo (§ 74-203(6)).</li>
    <li><strong>Actas.</strong> Cada reunión requiere actas escritas con los presentes, las mociones y los resultados de las votaciones, disponibles al público en un plazo razonable (§ 74-205). No se permiten votaciones secretas (§ 74-203(1)).</li>
    <li><strong>Un lugar físico.</strong> Se permiten reuniones remotas, pero por lo menos un miembro o el director de la agencia debe estar en el lugar anunciado para que el público pueda asistir (§ 74-203(5)).</li>
  </ul>
  <p>Lo que la ley <strong>no</strong> le da es el derecho a hablar. Vea <a href="speak-at-a-public-meeting.html">cómo hablar en una reunión pública local</a>.</p>

  <h2>Cuando un órgano no cumple la ley</h2>
  <ol>
    <li><strong>Avise por escrito.</strong> El órgano tiene 14 días para responder públicamente y, si está de acuerdo, otros 14 días para corregirlo declarando nulas las decisiones de esa reunión (§ 74-208(7)).</li>
    <li><strong>Presente una queja.</strong> El fiscal del condado (county prosecuting attorney) hace cumplir la ley para los órganos locales; el Fiscal General (Attorney General), para las agencias estatales (§ 74-208(5)). Los miembros que violan la ley a sabiendas pueden recibir multas personales.</li>
    <li><strong>Vaya a la corte.</strong> Cualquier persona afectada puede demandar. Una demanda para anular una decisión debe presentarse dentro de <strong>30 días</strong>; otras demandas, dentro de 180 días (§ 74-208(6)).</li>
  </ol>
""",
    sources=[(OML, "Manual de la Ley de Reuniones Abiertas de Idaho, julio de 2026, Fiscal General (en inglés)"),
             ("https://legislature.idaho.gov/statutesrules/idstat/Title74/T74CH2/", "Código de Idaho, Título 74, Capítulo 2 (en inglés)")])

G["public-records-requests"] = dict(
    cat="Local", title="Cómo pedir registros públicos en Idaho",
    lede="Correos electrónicos, contratos, presupuestos, informes policiales, paquetes de reuniones: casi todo lo que escriben los gobiernos de Idaho pertenece al público. Así se piden, cuánto cuestan, cuándo deben responder y qué hacer si le dicen que no.",
    body="""
  <h2>Qué puede pedir</h2>
  <p>Un registro público es cualquier documento sobre asuntos públicos que una agencia estatal o local prepara, posee, usa o guarda, en cualquier forma: papel, correo electrónico, mensajes de texto, hojas de cálculo, fotos o grabaciones (Código de Idaho § 74-101(13)). La ley cubre agencias estatales y todas las agencias locales: condados, ciudades, distritos escolares y distritos especiales.</p>
  <p>Cualquier persona puede pedirlos (§ 74-102(1)). En general, la agencia no puede preguntarle para qué los quiere. Tampoco tiene que crear un documento que no existe, así que pida documentos, no respuestas a preguntas.</p>

  <h2>Cómo hacer la solicitud</h2>
  <ol>
    <li><strong>Busque al encargado de registros</strong> ("records custodian"). Cada agencia debe tener uno. Busque "public records request" en el sitio web de la agencia; muchas tienen un formulario en línea.</li>
    <li><strong>Hágalo por escrito.</strong> El correo electrónico sirve. Diga claramente que es una solicitud de registros públicos. Puede escribir en español, pero la respuesta y los documentos probablemente estarán en inglés.</li>
    <li><strong>Describa los documentos con detalle,</strong> con un rango de fechas. Mientras más específica sea, más rápida y barata será la respuesta.</li>
    <li><strong>Incluya sus datos de contacto.</strong> La ley pide su nombre, dirección postal, correo y teléfono, y una declaración escrita de si vive en Idaho (§ 74-102(4)). La residencia cambia los plazos y costos. Significa haber vivido en Idaho por lo menos 30 días seguidos.</li>
    <li><strong>Diga cómo los quiere.</strong> Puede pedir copias electrónicas o revisarlos en persona.</li>
  </ol>
  <div class="callout">
    <p><strong>Una solicitud sencilla (en inglés, para enviar a la agencia)</strong></p>
    <p>"This is a public records request under Idaho Code &sect; 74-102. Please provide electronic copies of [describa los documentos] from [fecha de inicio] to [fecha final]. I am / am not an Idaho resident. My contact information: [nombre, dirección, correo, teléfono]. If any part of this request is denied, please cite the specific exemption and release the rest of the record with the exempt parts redacted."</p>
  </div>

  <h2>Plazos</h2>
  <ul>
    <li><strong>Residentes de Idaho:</strong> la agencia tiene <strong>3 días hábiles</strong> para aceptar o negar. Si necesita más tiempo, debe avisarle por escrito y entregarlos dentro de <strong>10 días hábiles</strong> (§ 74-103(2)).</li>
    <li><strong>No residentes:</strong> 21 días, que pueden extenderse a 35.</li>
    <li>Si pasa el plazo sin respuesta, la solicitud se considera negada (§ 74-103(3)).</li>
  </ul>

  <h2>Costo</h2>
  <ul>
    <li><strong>Para residentes de Idaho, las primeras dos horas de trabajo y las primeras 100 páginas son gratis</strong> (§ 74-102(10)(a)). Después, la agencia puede cobrar el costo real.</li>
    <li>Los cobros deben estar detallados, no en una sola cantidad.</li>
    <li><strong>Exención de pago:</strong> la agencia debe eximirle si los documentos ayudan al público a entender al gobierno, la solicitud no es principalmente para su beneficio personal y el costo le impediría obtenerlos (§ 74-102(10)(f)).</li>
  </ul>

  <h2>Lo que pueden negar</h2>
  <p>La ley tiene excepciones, y las agencias deben aplicarlas de manera estricta. Si un documento tiene partes exentas, deben tacharlas y entregarle el resto. Excepciones comunes: expedientes de personal (aunque el puesto y el salario de cada empleado público son públicos), investigaciones policiales activas, números de Seguro Social y asesoría legal.</p>

  <h2>Si le dicen que no</h2>
  <ol>
    <li><strong>Revise la carta de negación.</strong> Debe ser por escrito, citar la ley específica y explicarle su derecho a apelar (§ 74-103).</li>
    <li><strong>Intente aclarar o reducir la solicitud.</strong> Una llamada al encargado puede resolver mucho.</li>
    <li><strong>Vaya a la corte si es necesario.</strong> Puede presentar una petición en la corte de distrito del condado donde están los documentos dentro de <strong>180 días</strong> (§ 74-115). La corte debe fijar una audiencia dentro de 28 días.</li>
  </ol>
""",
    sources=[(PRM, "Manual de la Ley de Registros Públicos de Idaho, julio de 2026, Fiscal General (en inglés)"),
             ("https://legislature.idaho.gov/statutesrules/idstat/Title74/T74CH1/", "Código de Idaho, Título 74, Capítulo 1 (en inglés)")])

G["contact-your-representatives"] = dict(
    cat="Habilidades", title="Cómo comunicarse con quienes le representan",
    lede="Un mensaje corto y concreto de alguien que vive en el distrito sí se lee. Así se escoge la oficina correcta y esto es lo que debe decir el mensaje.",
    body="""
  <h2>Empiece con el nivel de gobierno correcto</h2>
  <ul>
    <li><strong>Ciudad:</strong> zonificación y permisos de construcción dentro de la ciudad, calles y banquetas, policía municipal, parques, agua y drenaje.</li>
    <li><strong>Condado:</strong> elecciones, avalúos de propiedad, el alguacil (sheriff) y la cárcel, el juzgado, y el uso de suelo fuera de la ciudad. Las licencias de manejo las da la oficina del alguacil del condado.</li>
    <li><strong>Distrito de carreteras:</strong> en muchas partes de Idaho, un distrito electo aparte se encarga de los caminos locales. En el condado de Ada, ACHD maneja casi todas las calles.</li>
    <li><strong>Estado:</strong> financiamiento escolar, carreteras estatales, prisiones, Medicaid, parques estatales y las leyes estatales.</li>
    <li><strong>Federal:</strong> Seguro Social y Medicare, beneficios para veteranos, inmigración, pasaportes, impuestos federales y las tierras federales.</li>
  </ul>
  <p>¿No sabe quiénes le representan? Use <a href="../../reps.html">la búsqueda por dirección</a> (en inglés).</p>

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
    <li><strong>Una llamada</strong> es rápida. Durante la sesión, el Centro de Información Legislativa es la puerta de entrada: 208-332-1000, o 800-626-0471 sin costo.</li>
    <li><strong>Fuera de la sesión,</strong> los legisladores están en sus distritos, y muchos tienen reuniones comunitarias. A menudo es el mejor momento para ser escuchado.</li>
    <li><strong>En persona</strong> funciona mejor a nivel local. Vea <a href="speak-at-a-public-meeting.html">cómo hablar en una reunión pública local</a>.</li>
  </ul>

  <h2>Cuando necesita ayuda, no un voto</h2>
  <p>Si tiene un problema con una agencia de gobierno, las oficinas de los funcionarios electos a menudo pueden ayudar. Los miembros del Congreso tienen personal que atiende problemas con agencias federales. Llame a la oficina y pida ayuda con un caso de constituyente ("constituent services").</p>
""",
    sources=[("https://legislature.idaho.gov/legislators/whosmylegislator/", "Who's My Legislator, Legislatura de Idaho (en inglés)"),
             ("https://legislature.idaho.gov/resources/committeetestimony/", "Cómo testificar ante comités legislativos (en inglés)")])
