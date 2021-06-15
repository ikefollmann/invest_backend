# Animations CSS - English
- Generate default classes for CSS3 Animations.

This is a simple jQuery/CSS plugin that will animate elements just by adding classes.
It uses jQuery plugin and CSS3.

## **How to use:**

Add to your _`<head>`_ tag:
```
<link href="css/gh_animation.min.css" rel="stylesheet" type="text/css" media="screen" />
<script type="text/javascript" src="js/gh_animation.min.js"></script>
```

Now you have to use classes to your elements that you want to animate. For exemple:

```
<div id="dieidi" class="bottom-to-fade">
  <p>I'm going to fade-in and roll over the document from the bottom to my original position!</p>
</div>
```

This will make your **dieidi** element become opacity 0 and 70px to bottom.
When your page loads and the element is at least 50% on viewport or you scroll to the element, **dieidi** will fade-in and move to it's original position.

What if I have tabs, for exemple, and I want to animate the elements when I switch tabs? Don't worry! All you have to do is add a simple line in your switch tab function:

```
dieidi.triggerAnim();
```

List of avaliable classes/effects:
* top-to-fade
* right-to
* right-to-fade
* bottom-to-fade
* left-to
* left-to-fade
* center-to-fade


# Animations CSS - Português
- Gera classes padrões de animações CSS3.

Um simples plugin jQuery/CSS que anima elementos apenas adicionando classes.
Esse plugin usa jQuery e CSS3.

## **Como Usar:**

Adicione na sua na sua tag _`<head>`_:
```
<link href="css/gh_animation.min.css" rel="stylesheet" type="text/css" media="screen" />
<script type="text/javascript" src="js/gh_animation.min.js"></script>
```

Agora você precisa usar classes nos elementos que você deseja animar. Por exemplo:

```
<div id="dieidi" class="bottom-to-fade">
  <p>Eu vou aparecer e rolar através do documento de baixo até minha posição original!</p>
</div>
```

Isso irá fazer com que o elemento **dieidi** fique com a opacidade 0 e 70px abaixo da posição original.
Quando a página carregar e o elemento estiver no mínimo 50% vísivel no campo de visão do documento ou quando você rolar até o elemento, **dieidi** vai aparecer e deslizar até sua posição original.

E se eu quiser animar os elementos quando eu trocar uma aba, por exemplo? Não se preocupe! Tudo que você precisa fazer é adicionar uma simples linha javascript na sua função de trocar abas:

```
dieidi.triggerAnim();
```

Lista de classes/efeitos disponíveis:
* top-to-fade
* right-to
* right-to-fade
* bottom-to-fade
* left-to
* left-to-fade
* center-to-fade


Animations CSS - Version 1.0

Copyright (c) 2016, AGÊNCIA GH - (http://agenciagh.com.br/)
