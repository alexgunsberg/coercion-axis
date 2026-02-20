#!/usr/bin/env python3
"""
Pakkoakseli - Simulator
A tool to run simulations on the Coercion Axis scoring algorithm.
"""

import random

def calculate_score(scores):
    """
    Calculates the Pakkoakseli score based on an array of 35 answers.
    Each answer is in [-4, -2, 0, 2, 4].
    Negative = Libertarian / Freedom
    Positive = Statist / Coercion
    """
    if len(scores) != 35:
        raise ValueError(f"Expected 35 answers, got {len(scores)}")

    liberty = sum(abs(s) for s in scores if s < 0)
    statist = sum(s for s in scores if s > 0)
    
    total = liberty + statist
    pct = (liberty / total * 100) if total > 0 else 50
    
    return liberty, statist, pct

def simulate_random_users(count=10000):
    print(f"Simulating {count} random users...")
    options = [-4, -2, 0, 2, 4]
    
    lib_dominant = 0
    stat_dominant = 0
    neutral = 0
    
    for _ in range(count):
        scores = [random.choice(options) for _ in range(35)]
        liberty, statist, pct = calculate_score(scores)
        
        if pct > 50:
            lib_dominant += 1
        elif pct < 50:
            stat_dominant += 1
        else:
            neutral += 1
            
    print(f"Results of {count} simulations:")
    print(f"Libertarian dominant: {lib_dominant} ({(lib_dominant/count)*100:.1f}%)")
    print(f"Statist dominant: {stat_dominant} ({(stat_dominant/count)*100:.1f}%)")
    print(f"Neutral: {neutral} ({(neutral/count)*100:.1f}%)")

def main():
    print("=== Pakkoakseli Simulator ===")
    
    # Example 1: Perfect Libertarian
    scores_lib = [-4] * 35
    l, s, p = calculate_score(scores_lib)
    print(f"Perfect Libertarian (-4 all): {l}/{s} -> {p:.1f}% Libertarian")
    
    # Example 2: Perfect Statist
    scores_stat = [4] * 35
    l, s, p = calculate_score(scores_stat)
    print(f"Perfect Statist (+4 all): {l}/{s} -> {p:.1f}% Libertarian")
    
    # Example 3: Neutral
    scores_neu = [0] * 35
    l, s, p = calculate_score(scores_neu)
    print(f"Perfect Neutral (0 all): {l}/{s} -> {p:.1f}% Libertarian")
    print()
    
    simulate_random_users()

if __name__ == "__main__":
    main()
