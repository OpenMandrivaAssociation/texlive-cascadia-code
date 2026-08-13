%global tl_name cascadia-code
%global tl_revision 77682
%global tl_version 0.0.2

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	The Cascadia Code font with support for LaTeX and pdfLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/cascadia-code
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cascadia-code.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cascadia-code.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Cascadia Code is a monospaced font by Microsoft. This package provides
the Cascadia Code family of fonts with support for LaTeX and pdfLaTeX.
Adding \usepackage{cascadia-code} to the preamble of your document will
activate Cascadia Code as the typewriter font (\ttdefault).


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from cascadia-code:
Map CascadiaCode.map
TL_DROPIN_EOF
