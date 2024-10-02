# Statistiques inférentielles: Rappels

Soit $X$ une variable aléatoire suivant une loi **inconnue** de moyenne $\mu$ et de variance $\sigma^2$.
Soit $(X_1, X_2, \cdots, X_n)$ un échantillon de $n$ variables aléatoires *indépendantes identiquement distribuées* (i.i.d.) alors :

+ $\bar{X} = \frac{1}{n}\sum_i^n X_i$ est **un** estimateur de $\mu$.  

+ $E[\bar{X}] = \mu$ et $var[\bar{X}] = \frac{\sigma^2}{n}$     $\bar{X}$ est un estimateur sans biais et consistant de $\mu$.

+ $\bar{X} \sim N(\mu, \frac{\sigma^2}{n})$  si $n>30$ : $\bar{X}$ suit une loi normale (Théorème Central Limite) et ce **quelle que soit la loi initiale** de X 

+ $s^2 = \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X})$  est **un** estimateur de $\sigma^2$

+ $E[s^2] = \sigma^2$ et $var[s^2]= 2 \frac{(N-1)\sigma^4}{N^2}$ $s^2$ est un estimateur sans biais et consistant de $\sigma^2$. 

+ Dans les cas où $(X_1, X_2, \cdots, X_n)$ est un échantillon de **$n$ variables aléatoires indépendantes gaussiennes** 

  $\frac{n^2 s^2}{\sigma^2} \sim \chi_2(n-1)$ : la loi de la variance empirique est connue ou $\chi_2 (k) = \sum_{i=1}^k Y^2_i$ avec $Y_i \sim N(0,1)$

**Estimation ponctuelle de $\mu$**

$\hat{\mu} = \bar{X}$

**Estimation ponctuelle de $\sigma^2$** 

$\hat{\sigma^2}$ = $s^2$

**Estimation par intervalle de confiance de $\mu$**

1. **$\sigma$ est connue** 

$$\{ \bar{X} - \frac{\sigma}{\sqrt{n}} u_{1-\frac{\alpha}{2}}, \bar{X} + \frac{\sigma}{\sqrt{n}} u_{1-\frac{\alpha}{2}} \}$$

+ Remarque l'intervalle est aléatoire (car $\bar{X}$ est une variable aléatoire ) centré en  $\bar{X}$  et de largeur $2*\frac{\sigma}{\sqrt{n}} u_{1-\frac{\alpha}{2}}$ 
+ L'intervalle de confiance tend vers $\bar{X}$ quand $n$ tend vers $+\infin$

2. **$\sigma$ est inconnue**

$$\{ \bar{X} - \frac{S^{*}}{\sqrt{n}} t_{1-\frac{\alpha}{2}}(n-1), \bar{X} + \frac{S^*}{\sqrt{n}} t_{1-\frac{\alpha}{2}}(n-1) \}$$

> Remarque l'intervalle est aléatoire (car $\bar{X}$ et $S^{*}$ sont des variables aléatoires),  centré en  $\bar{X}$  et de largeur $2*\frac{(n-1) s^*}{\sqrt{n}} t_{1-\frac{\alpha}{2}}$ 





###### 
