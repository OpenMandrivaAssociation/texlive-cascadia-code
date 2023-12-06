Name:		texlive-cascadia-code
Version:	68485
Release:	1
Summary:	The Cascadia Code font with support for LaTeX and pdfLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cascadia-code
License:	ofl lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cascadia-code.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cascadia-code.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Cascadia Code is a monospaced font by Microsoft. This package
provides the Cascadia Code family of fonts with support for
LaTeX and pdfLaTeX. Adding \usepackage{cascadia-code} to the
preamble of your document will activate Cascadia Code as the
typewriter font (\ttdefault).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/cascadia-code
%{_texmfdistdir}/fonts/vf/public/cascadia-code
%{_texmfdistdir}/fonts/type1/public/cascadia-code
%{_texmfdistdir}/fonts/tfm/public/cascadia-code
%{_texmfdistdir}/fonts/opentype/public/cascadia-code
%{_texmfdistdir}/fonts/map/dvips/cascadia-code
%{_texmfdistdir}/fonts/enc/dvips/cascadia-code
%doc %{_texmfdistdir}/doc/fonts/cascadia-code

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
