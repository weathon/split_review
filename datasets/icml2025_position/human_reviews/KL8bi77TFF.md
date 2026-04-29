## Human Reviewer 1

### Questions
Regarding (2) and (3), what happens when x and/or x' are in an area of the input space where no natural looking images exist? In that case, the error (disagreement of f and g) is perhaps less relevant/irrelevant. The footnote touches on this in suggesting that when g is not confident, things are different. But this point is not adequately explored. Given that legitimate inputs are on a submanifold of the huge R^d input space, then I am not sure if having an oracle g defined everywhere is well defined/makes sense. And certainly comparison with it is not sensible at all points.

Re equation (2), it is symmetric in x and x', so that if x' is an adv sample for x, then x is for x'. This is not necessarily wrong, but feels odd. Perhaps there needs to be a constraint re x being a legitimate image?? (whatever that may mean!) 

Does (2) also need the condition that f(x)=g(x), so that x' is really an adversarial example and it is not just that f is wrong at and near x?

"Robust features will help alleviate backdoor attacks". Why? Is there a citation for this?

It is mentioned that adversarial robustness and generalisation  are two sides of the same coin. But surely by equation (3), if that is being put forward as a robustness measure, you are almost identifying them (same side of coin) as you are requiring f to generalise from its training data to agree with some (mythical) oracle precisely everywhere as a definition of robustness. But this seems to be a measure of generalisation success from the training data too. 

Is it clear, as is claimed, that current neural network architectures cannot solve the general problem (assuming it could be well-posed)? ie since it can be argued that it follows from the universal approximation theorem that it should be possible (though resource limits may be a factor).

Is there a citation for the statement that the human visual system has sacrificed negligible accuracy in order to gain robustness?

### Rating
1

### Confidence
3

---

## Human Reviewer 2

### Questions
Please refer to the weaknesses listed in Section “Strengths and Weaknesses”.

### Rating
2

### Confidence
5

---

## Human Reviewer 3

### Questions
1. Authors argue that the bounded perturbation assumption is restrictive and misleading. How would authors propose to formally define and evaluate robustness in the expanded framework? What metrics would replace the current $\ell_p$-norm constraints?

2. Imperceptible perturbations may be a main concern in some sensitive areas, how do authors reconcile the position with this?

### Rating
3

### Confidence
3

---

## Human Reviewer 4

### Questions
What is $g$ in Eq. (2)?

### Rating
1

### Confidence
4