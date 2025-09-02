let respostaCorreta = 0;

function iniciarJogo(operacao) {
  const num1 = Math.floor(Math.random() * 10 + 1);
  const num2 = Math.floor(Math.random() * 10 + 1);
  let pergunta = '';

  switch (operacao) {
    case 'adicao':
      respostaCorreta = num1 + num2;
      pergunta = `${num1} + ${num2}`;
      break;
    case 'subtracao':
      respostaCorreta = num1 - num2;
      pergunta = `${num1} - ${num2}`;
      break;
    case 'multiplicacao':
      respostaCorreta = num1 * num2;
      pergunta = `${num1} × ${num2}`;
      break;
    case 'divisao':
      const produto = num1 * num2;
      respostaCorreta = num1;
      pergunta = `${produto} ÷ ${num2}`;
      break;
  }

  document.getElementById('pergunta').textContent = `Quanto é ${pergunta}?`;
  document.getElementById('resposta').value = '';
  document.getElementById('resultado').textContent = '';
}

function verificarResposta() {
  const respostaUsuario = parseFloat(document.getElementById('resposta').value);

  if (respostaUsuario === respostaCorreta) {
    document.getElementById('resultado').textContent = '✅ Resposta correta!';
    document.getElementById('resultado').style.color = 'green';
  } else {
    document.getElementById('resultado').textContent = `❌ Errado. A resposta correta é ${respostaCorreta}.`;
    document.getElementById('resultado').style.color = 'red';
  }
}
