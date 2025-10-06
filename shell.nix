# Nix environment configuration
{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python3
    python3Packages.numpy
    python3Packages.pytest
    python3Packages.pytest-cov
    python3Packages.black
    python3Packages.flake8
  ];

  shellHook = ''
    echo "🐍 Nix Python environment loaded!"
    echo "Run 'pytest' to execute tests"
  '';
}