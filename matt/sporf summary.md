# Sparse Projection Oblique Randomer Forests

## Summary

SPORF (Sparse Projection Oblique Randomer Forests) is a type of decision forest, meaning it is an ensemble of decision trees. Typically, decision forests use axis-aligned decision trees, but many methods use axis-oblique splits. The methods that have axis-oblique splits have many shortcomings - SPORF uses axis-oblique splits while outperforming other decision forests in many cases. SPORF is used for classification tasks, but an implemention for regression tasks is in development.

How SPORF Works

SPORF searches for splits over sparse random prejections
> Sample ceil(λpd) non-zero numbers from {-1,+1} with equal probabilities

Shortcomings SPORF Addresses

1. Random Search for Splits are more efficient and overfit less than supervised search procedures
2. Flexible sparsity means SPORF performs well in high-dimensional settings
3. SPORF does not introduce many new hyperparameters to tune - just a factor lambda to control the sparsity
4. SPORF is interpretable to learn about the data (unlike typical oblique decision forests)
5. SPORF is fast and scalable

Results
1. SPORF performs well on standard benchmarks, over RF, XGBoost, RR-RF< and CCF.
2. SPORF is robust to high-dimensional noise.
3. SPORF performs better (higher accuracy) with relatively more comptutation. It is faster in practice than RF but not F-RC (which splits on linear combinations of coordinates rather than individual coordinates).
4. "SPORF can outperform other algorithms because of stronger trees and/or less correlated trees. Therefore, SPORF perhaps offers more flexible control over the balance between tree strength and correlation, thereby allowing it to adapt better to different problems."

