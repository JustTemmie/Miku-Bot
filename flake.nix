{
  description = "miku dev flake, made for fish";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-25.11";
  };

  outputs = { self, nixpkgs }:
  let
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
  in {
    devShells.${system}.default = pkgs.mkShell {
      nativeBuildInputs = [
        pkgs.python3
        pkgs.libopus

        pkgs.ffmpeg
        pkgs.poppler
      ];

      LIBOPUS_PATH = "${pkgs.libopus}/lib/libopus.so";
      FFMPEG_PATH = "${pkgs.ffmpeg}/bin/ffmpeg";
      FFPROBE_PATH = "${pkgs.ffmpeg}/bin/ffprobe";
      POPPLER_PATH = "${pkgs.poppler}/lib/";

      shellHook = ''
      '';
    };
  };
}
