# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/pspicture
# catalog-date 2007-03-11 16:56:01 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-pspicture
Version:	20070311
Release:	7
Summary:	PostScript picture support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pspicture
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pspicture.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pspicture.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pspicture.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A replacement for LaTeX's picture macros, that uses PostScript
\special commands. The package is now largely superseded by
pict2e.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pspicture/pspicture.ps
%{_texmfdistdir}/tex/latex/pspicture/pspicture.sty
%doc %{_texmfdistdir}/doc/latex/pspicture/README
%doc %{_texmfdistdir}/doc/latex/pspicture/pspicture.pdf
#- source
%doc %{_texmfdistdir}/source/latex/pspicture/pspicture.dtx
%doc %{_texmfdistdir}/source/latex/pspicture/pspicture.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070311-2
+ Revision: 755152
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070311-1
+ Revision: 719325
- texlive-pspicture
- texlive-pspicture
- texlive-pspicture
- texlive-pspicture

